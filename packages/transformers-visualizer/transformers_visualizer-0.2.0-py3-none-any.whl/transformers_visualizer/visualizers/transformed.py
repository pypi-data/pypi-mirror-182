# from copy import deepcopy
# from typing import List, Optional, Set, Tuple, Union

# import torch
# from captum.attr import LayerActivation
# from transformers import PreTrainedModel, PreTrainedTokenizer, PreTrainedTokenizerFast
# from transformers.tokenization_utils_base import BatchEncoding

# from transformers_visualizer.errors import OutputNotComputedEror
# from transformers_visualizer.plotting import plot_token_to_head_specific_dimension
# from transformers_visualizer.visualizer import Visualizer

# # TODO: interpretable_embedding  + gorokoba560/norm-analysis-of-transformer


# class TokenToHeadScore(Visualizer):
#     """
#     Visualizer for plotting token-to-head importance scores.
#     """

#     def __init__(
#         self,
#         model: PreTrainedModel,
#         tokenizer: Union[PreTrainedTokenizer, PreTrainedTokenizerFast],
#         device: Optional[Union[torch.device, str]] = None,
#     ) -> None:
#         """
#         Create a token-to-head score visualizer. Visualize transformed vector (i.e. `hidden_state` in transformers-based models context).

#         Args:
#             model (PreTrainedModel): _description_
#             tokenizer (Union[PreTrainedTokenizer, PreTrainedTokenizerFast]): _description_
#             device (Optional[Union[torch.device, str]], optional): _description_. Defaults to None.
#         """
#         super().__init__(model, tokenizer, device)
#         self.model.config.output_attentions = True
#         self.model.config.output_hidden_states = True

#     def set_device(self, value: Union[torch.device, str]) -> None:
#         """
#         Set a `torch.device`.

#         Args:
#             value (Union[torch.device, str]): A `torch.device` or a `str`.

#         Raises:
#             ValueError: raised if `value` isn't a `torch.device` or acceptable `str`.
#         """
#         super().set_device(value)

#     def _forward(self, inputs, ids: BatchEncoding):
#         ids = deepcopy(ids)
#         ids.pop("input_ids", "None")
#         pred = self.model({**inputs, **ids.to(self.device)})
#         return pred.last_hidden_state

#     def __call__(self, text: str) -> None:
#         """
#         Given a text input generates necessary elements for visualization. Multiple text input is not supported.

#         Args:
#             text (str): Text input.
#         """
#         if (
#             isinstance(text, List) or isinstance(text, Tuple) or isinstance(text, Set)  # type: ignore
#         ):
#             raise NotImplementedError("Multiple text input is not supported.")

#         self.tokens = self.tokenizer(text, return_tensors="pt").to(self._device)
#         self.all_tokens: List[str] = self.tokenizer.convert_ids_to_tokens(
#             self.tokens["input_ids"].squeeze().tolist()  # type: ignore
#         )

#         self.output = self.model(**self.tokens)
#         self.attentions = torch.concat(self.output.attentions)

#         # n_layers = len(self.model.base_model.encoder.layer)  # type: ignore
#         n_layers = self.model.config.num_hidden_layers
#         n_heads = self.model.config.num_attention_heads
#         head_size = (
#             self.model.config.hidden_size // self.model.config.num_attention_heads
#         )
#         all_head_size = self.model.config.hidden_size

#         # Getting Access to Value Activations

#         layers = [
#             self.model.base_model.encoder.layer[layer].attention.self.value  # type: ignore
#             for layer in range(n_layers)
#         ]
#         input_embeddings = self.output.hidden_states[0]

#         la = LayerActivation(self._forward, layers)
#         value_layer_acts = la.attribute(
#             input_embeddings, additional_forward_args=(self.tokens)
#         )
#         # shape -> layer x seq_len x all_head_size
#         value_layer_acts = torch.concat(value_layer_acts)
#         new_x_shape = value_layer_acts.size()[:-1] + (n_heads, head_size)
#         value_layer_acts = value_layer_acts.view(*new_x_shape)

#         # layer x num_heads x 1 x head_size
#         value_layer_acts = (
#             value_layer_acts.permute(0, 1, 3, 2).permute(0, 1, 3, 2, 4).contiguous()
#         )
#         # layer x seq_length x num_heads x 1 x head_size
#         value_layer_acts = value_layer_acts.view(
#             value_layer_acts.size()[:-1]
#             + (
#                 1,
#                 value_layer_acts.size()[-1],
#             )
#         )

#         # Getting Access to Dense Features
#         dense_acts = torch.stack(
#             [
#                 dlayer.attention.output.dense.weight
#                 for dlayer in self.model.bert.encoder.layer  # type: ignore
#             ]
#         )
#         dense_acts = dense_acts.view(len(layers), all_head_size, n_heads, head_size)
#         # layer x num_heads x head_size x all_head_size
#         dense_acts = dense_acts.permute(0, 2, 3, 1).contiguous()

#         # layers, seq_length, num_heads, 1, all_head_size
#         f_x = torch.stack(
#             [
#                 value_layer_acts_i.matmul(dense_acts_i)
#                 for value_layer_acts_i, dense_acts_i in zip(
#                     value_layer_acts, dense_acts
#                 )
#             ]
#         )
#         # layer x seq_length x num_heads x 1 x all_head_size)
#         f_x = f_x.view(f_x.size()[:-2] + (f_x.size()[-1],))
#         f_x = f_x.permute(0, 1, 3, 2).contiguous()

#         self.f_x = f_x
#         self.f_x_normalized = torch.linalg.norm(self.f_x, dim=-1)

#     def compute(self, text: str):
#         """
#         Given a text input generates necessary elements for visualization. Multiple text input is not supported. Work in place.

#         Args:
#             text (str): Text input.
#         """
#         return super().compute(text)

#     def plot(self, **plot_kwargs) -> None:
#         """
#         Plot the Visualizer. The purpose of kwargs are used to setup plotting parameters.

#         Args:
#             figsize (Tuple[int, int], optional): Figsize of the plot. Defaults to (20, 20).
#             ticks_fontsize (int, optional): Ticks fontsize. Defaults to 7.
#             title_fontsize (int, optional): Title fontsize. Defaults to 9.
#             cmap (str, optional): Colormap. Defaults to "viridis".
#             colorbar (bool, optional): Display colorbars. Defaults to True.

#         Raises:
#             OutputNotComputedEror: raised if no `Output` present.
#         """
#         if (
#             not hasattr(self, "attentions")
#             or hasattr(self, "f_x_normalized")
#             or not hasattr(self, "all_tokens")
#         ):
#             raise OutputNotComputedEror

#         plot_token_to_head_specific_dimension(
#             self.attentions,
#             self.all_tokens,
#             "Layer",
#             **plot_kwargs,
#         )

#     def __str__(self) -> str:
#         return super().__str__()


# # def _visualize_token2head_scores(scores_mat, all_tokens):
# #     fig = plt.figure(figsize=(15, 15))

# #     for idx, scores in enumerate(scores_mat):
# #         scores_np = np.array(scores)
# #         ax = fig.add_subplot(6, 2, idx + 1)
# #         # append the attention weights
# #         im = ax.matshow(scores_np, cmap="viridis")

# #         fontdict = {"fontsize": 8}

# #         ax.set_xticks(range(len(all_tokens)))
# #         ax.set_yticks(range(len(scores)))

# #         ax.set_xticklabels(all_tokens, fontdict=fontdict, rotation=90)
# #         # ax.set_yticklabels(range(len(scores[0])), fontdict=fontdict)
# #         ax.set_yticklabels(range(len(scores)), fontdict=fontdict)
# #         ax.set_xlabel("Layer {}".format(idx + 1))

# #         fig.colorbar(im, fraction=0.046, pad=0.04)
# #     plt.tight_layout()
# #     return plt.gcf()


# # def _forward(inputs, model, ids, device):
# #     pred = model(
# #         ids["input_ids"].to(device),
# #         ids["attention_mask"].to(device))
# #     return pred.logits.max(1).values


# # def visualize_vector_norm(
# #     device, model, description, tokenizer, preprocessing_func=None, compute="norm", layer=None
# # ):
# #     if preprocessing_func is not None:
# #         description = preprocessing_func(description)
# #     all_tokens = tokenizer.convert_ids_to_tokens(tokenizer(description)["input_ids"])
# #     ids = tokenizer.encode_plus(
# #         description,
# #         truncation=True,
# #         padding=True,
# #         max_length=512,
# #         return_attention_mask=True,
# #         return_tensors="pt",
# #     )
# #     output = model(
# #         ids["input_ids"].to(device),
# #         ids["attention_mask"].to(device),
# #     )
# #     attentions = output.attentions
# #     output_attentions_all = torch.stack(attentions)

# #     output_attentions_all_shape = output_attentions_all.shape
# #     batch = output_attentions_all_shape[1]
# #     num_heads = output_attentions_all_shape[2]
# #     head_size = 64
# #     all_head_size = 768

# #     layers = [
# #         model.base_model.encoder.layer[layer].attention.self.value
# #         for layer in range(len(model.base_model.encoder.layer))
# #     ]

# #     input_embeddings = output.hidden_states[0]

# #     la = captum.attr.LayerActivation(_forward, layers)
# #     value_layer_acts = la.attribute(input_embeddings, additional_forward_args=(
# #         model,
# #         ids,
# #         device
# #     ))
# #     # shape -> layer x batch x seq_len x all_head_size
# #     value_layer_acts = torch.stack(value_layer_acts)

# #     new_x_shape = value_layer_acts.size()[:-1] + (num_heads, head_size)
# #     value_layer_acts = value_layer_acts.view(*new_x_shape)

# #     # layer x batch x neum_heads x 1 x head_size
# #     value_layer_acts = value_layer_acts.permute(0, 1, 3, 2, 4)

# #     value_layer_acts = value_layer_acts.permute(0, 1, 3, 2, 4).contiguous()
# #     value_layer_acts_shape = value_layer_acts.size()

# #     # layer x batch x seq_length x num_heads x 1 x head_size
# #     value_layer_acts = value_layer_acts.view(value_layer_acts_shape[:-1] + (1, value_layer_acts_shape[-1],))

# #     dense_acts = torch.stack([dlayer.attention.output.dense.weight for dlayer in model.base_model.encoder.layer])
# #     dense_acts = dense_acts.view(len(layers), all_head_size, num_heads, head_size)

# #     # layer x num_heads x head_size x all_head_size
# #     dense_acts = dense_acts.permute(0, 2, 3, 1).contiguous()

# #     # layers, batch, seq_length, num_heads, 1, all_head_size
# #     f_x = torch.stack([value_layer_acts_i.matmul(dense_acts_i) for value_layer_acts_i, dense_acts_i in zip(value_layer_acts, dense_acts)])

# #     # layer x batch x seq_length x num_heads x 1 x all_head_size)
# #     f_x_shape = f_x.size()
# #     f_x = f_x.view(f_x_shape[:-2] + (f_x_shape[-1],))
# #     f_x = f_x.permute(0, 1, 3, 2, 4).contiguous()

# #     #(layers x batch, num_heads, seq_length, all_head_size)
# #     f_x_shape = f_x.size()


# #     # ||f(x)||
# #     #(layers x batch, num_heads, seq_length)
# #     f_x_norm = torch.linalg.norm(f_x, dim=-1)
# #     if compute == "norm":
# #         _visualize_token2head_scores(f_x_norm.squeeze().detach().cpu().numpy(), all_tokens)


# #     # ||alpha * f(x)||
# #     # layer x batch x num_heads x seq_length x seq_length x all_head_size
# #     alpha_f_x = torch.einsum('lbhks,lbhsd->lbhksd', output_attentions_all, f_x)

# #     # layer x batch x num_heads x seq_length x seq_length
# #     alpha_f_x_norm = torch.linalg.norm(alpha_f_x, dim=-1)
# #     if compute == "alpha-norm":
# #         _visualize_token2token_scores(
# #             alpha_f_x_norm[layer].squeeze().detach().cpu().numpy(),
# #             all_tokens,
# #             "Head"
# #         )

# #     # || SUM alpha * f(x)||
# #     summed_alpha_f_x = alpha_f_x.sum(dim=2)

# #     # layers x batch x seq_length x seq_length
# #     summed_alpha_f_x_norm = torch.linalg.norm(summed_alpha_f_x, dim=-1)
# #     if compute == "sum-norm":
# #         _visualize_token2token_scores(
# #             summed_alpha_f_x_norm.squeeze().cpu().detach().numpy(),
# #             all_tokens,
# #             "Layer"
# #         )
