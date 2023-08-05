# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_pydantic']

package_data = \
{'': ['*']}

install_requires = \
['dagster>=1.1.7,<2.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'dagster-pydantic',
    'version': '0.1.0',
    'description': '',
    'long_description': '# dagster-pydantic\n\nThis is a naive approach for using Pydantic types for Dagster Type Checking. The\npackage `dagster_pydantic` includes a really simple validation factory. Pydanitc\nis not built as a data validation library, it\'s actually a great parser and an\nOK validator in that order.\n\nThe purpose of this validation step is to ensure the shape of the model is\ncorrect before the data is consumed by the next op. Pydantic will stop you\nduring the instantiation of your model if the data is not up to spec but if you\nwant to check if the shape of the parsed data will match the model, that\'s where\nthe validation layer comes in.\n\n## Usage\n\n```python\nclass MyPydanticModel(BaseModel):\n    """\n    This is a Pydantic model.\n    """\n    a: int\n    b: str\n\n\nMyPydanticModelDT = pydantic_to_dagster_type(MyPydanticModel)\n\n@op(out=Out(MyPydanticModelDT))\ndef get_model():\n    model = MyPydanticModel(\n        a = 1,\n        b = "hello"\n    )\n    # This should fail type checking in the Dagit UI.\n    model.b = {} # type: ignore\n    return model\n```\n\nThis code will result in:\n\n![A typechecking error in the dagit UI](./screenshot1.png)\n\nWithout this integration, you wouldn\'t see that typechecking error in the\nconsole and the next op will consume a `dict` in place of a `str`.\n\n## Developing\n\nFirst, install [Just](https://github.com/casey/just)\n\n```sh\n$ just install\n```\n\nThis will run two poetry commands in your current terminal, one that configures\nvenvs to be in the project directory so the dependencies are accessable from\nyour local environment. The other will install the dependencies.\n\n```sh\n$ just shell\n```\n\nThis opens a current shell into your poetry virtual env.\n\nRunning tests\n\n```sh\n$ just test # This only runs pytest\n```\n\n## Disclaimer\n\nI\'ve only had my hands on Dagster for a few weeks. I love the declarative\nframework, and the focus on flexibility + developer velocity. I am a bit iffy on\nthe pricing and what\'s offered in the "Standard plan", but otherwise I\'m so\nimpressed by the open-source project.\n\nThat being said, I\'m a noobie. This is my first integration and also my first\nPython module, so feel free to drop an issue if there\'s something I\'m missing.\n',
    'author': 'Mitchell Hynes',
    'author_email': 'ecumene@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
