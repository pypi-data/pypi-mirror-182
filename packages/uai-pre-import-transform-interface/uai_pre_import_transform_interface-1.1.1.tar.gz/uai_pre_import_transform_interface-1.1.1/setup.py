# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uai_pre_import_transform_interface']

package_data = \
{'': ['*']}

install_requires = \
['uai-uri-interface>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'uai-pre-import-transform-interface',
    'version': '1.1.1',
    'description': '',
    'long_description': '# General\nThis package provides an Interface that can be implemented to then be turned into a job.\nThe used URI interface (`from uai_pre_transform_interface import URI`) is basically a [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) with some missing functionality.\n\n# WARNING: URI is not a local file\n**Beware**: Inside understand.ai we will hand cloud paths as URIs. So using the string of a path to open it will fail in these cases!\nE.g. Do **not** do things like this:\n```python\nfrom uai_pre_import_transform_interface import PreImportTransformInterface, URI\nfrom PIL import Image\n\nclass PreImportTransformer(PreImportTransformInterface):\n    def transform(self, input_path: URI, output_path: URI):\n        path_to_image = input_path / "images" / "00001.png"\n        with Image.open(str(path_to_image)) as im:  # This will fail if input path is "gs://dataset/clip1/"\n            im.show()\n```\ninstead you could do\n```python\nfrom uai_pre_import_transform_interface import PreImportTransformInterface, URI\nfrom PIL import Image\nfrom tempfile import NamedTemporaryFile\n\nclass PreImportTransformer(PreImportTransformInterface):\n    def transform(self, input_path: URI, output_path: URI):\n        path_to_image = input_path / "images" / "00001.png"\n        \n        # example for when your method takes readable bytes\n        with Image.open(path_to_image.open("rb")) as im:\n            im.show()\n\n        # example for when your method needs just a path to the file\n        with NamedTemporaryFile() as tmp:\n            tmp.write(path_to_image.open("rb").read())\n            Image.open(tmp.name)\n```\n\n**Unit tests do not catch this, unfortunately**. One idea to be more save against this could be to not use pathlib.Path directly for debugging but to instead extend path with an implementation that raises an error on usage of `__str__`.\n```python\nfrom pathlib import Path\n\nclass DebuPath(Path):\n    def __str__(self):\n        raise Exception("it is not a good idea to use strings for paths for anything but logging as these paths could point to remote resources.")\n```\n\n# Implementation\nEvery implementation should provide a python package named by you. Let\'s use `package_name` as an example. From this package the following import has to work:\n```python\nfrom package_name import PreImportTransformer\n```\nThis should give your implementation of the interface. To achieve this the `__init__.py` oyour package should contain something like this (depending on how you name things):\n```python\nfrom .my_interface_implementation import PreImportTransformer\n__all__: Sequence[str] = ["PreImportTransformer"]\n```\n\nThis is how we will automatically bind your library into our system. ![img.png](package_architecture.png)\n',
    'author': 'understand.ai',
    'author_email': 'postmaster@understand.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
