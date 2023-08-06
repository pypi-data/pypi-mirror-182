# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['transformers_visualizer', 'transformers_visualizer.visualizers']

package_data = \
{'': ['*']}

install_requires = \
['captum>=0.5.0',
 'matplotlib>=3.5',
 'torchtyping>=0.1.4',
 'transformers>=4.0.0']

setup_kwargs = {
    'name': 'transformers-visualizer',
    'version': '0.2.1',
    'description': 'Explain your 🤗 transformers without effort! Display the internal behavior of your model.',
    'long_description': '<h1 align="center">Transformers visualizer</h1>\n<p align="center">Explain your 🤗 transformers without effort!</p>\n<h1 align="center"></h1>\n\n<p align="center">\n    <a href="https://opensource.org/licenses/Apache-2.0">\n        <img alt="Apache" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">\n    </a>\n    <a href="https://github.com/VDuchauffour/transformers-visualizer">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/transformers-visualizer?label=version">\n    </a>\n</p>\n\nTransformers visualizer is a python package designed to work with the [🤗 transformers](https://huggingface.co/docs/transformers/index) package. Given a `model` and a `tokenizer`, this package supports multiple ways to explain your model by plotting its internal behavior.\n\nThis package is mostly based on the [Captum][Captum] tutorials [[1]][captum_part1] [[2]][Captum_part2].\n\n## Installation\n\n```shell\npip install transformers-visualizer\n```\n\n## Quickstart\n\nLet\'s define a model, a tokenizer and a text input for the following examples.\n\n```python\nfrom transformers import AutoModel, AutoTokenizer\n\nmodel_name = "bert-base-uncased"\nmodel = AutoModel.from_pretrained(model_name)\ntokenizer = AutoTokenizer.from_pretrained(model_name)\ntext = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder."\n```\n\n### Visualizers\n\n<details><summary>Attention matrices of a specific layer</summary>\n\n<p>\n\n```python\nfrom transformers_visualizer import TokenToTokenAttentions\n\nvisualizer = TokenToTokenAttentions(model, tokenizer)\nvisualizer(text)\n```\n\nInstead of using `__call__` function, you can use the `compute` method. Both work in place, `compute` method allows chaining method.\n\n`plot` method accept a layer index as parameter to specify which part of your model you want to plot. By default, the last layer is plotted.\n\n```python\nimport matplotlib.pyplot as plt\n\nvisualizer.plot(layer_index = 6)\nplt.savefig("token_to_token.jpg")\n```\n\n<p align="center">\n    <img alt="token to token" src="https://raw.githubusercontent.com/VDuchauffour/transformers-visualizer/main/images/token_to_token.jpg" />\n</p>\n\n</p>\n\n</details>\n\n<details><summary>Attention matrices normalized across head axis</summary>\n\n<p>\n\nYou can specify the `order` used in `torch.linalg.norm` in `__call__` and `compute` methods. By default, it\'s a L2 norm.\n\n```python\nfrom transformers_visualizer import TokenToTokenNormalizedAttentions\n\nvisualizer = TokenToTokenNormalizedAttentions(model, tokenizer)\nvisualizer.compute(text).plot()\n```\n\n<p align="center">\n    <img alt="normalized token to token"src="https://raw.githubusercontent.com/VDuchauffour/transformers-visualizer/main/images/token_to_token_normalized.jpg" />\n</p>\n\n</p>\n\n</details>\n\n## Upcoming features\n\n- [ ] Adding an option to specify head/layer indices to plot.\n- [ ] Adding other plotting backends such as Plotly, Bokeh, Altair.\n- [ ] Implement other visualizers such as [vector norm](https://arxiv.org/pdf/2004.10102.pdf).\n\n## References\n\n- [[1]][captum_part1] Captum\'s BERT example part 1\n- [[2]][captum_part2] Captum\'s BERT example part 2\n\n## Acknowledgements\n\n- [Transformers Interpret](https://github.com/cdpierse/transformers-interpret) for the idea of this project.\n\n[Captum]: https://captum.ai/\n[captum_part1]: https://captum.ai/tutorials/Bert_SQUAD_Interpret\n[Captum_part2]: https://captum.ai/tutorials/Bert_SQUAD_Interpret2',
    'author': 'VDuchauffour',
    'author_email': 'vincent.duchauffour@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/VDuchauffour/transformers-visualizer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
