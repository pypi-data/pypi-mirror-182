# General
This package provides an Interface that can be implemented to then be turned into a job.
The used URI interface (`from uai_pre_transform_interface import URI`) is basically a [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path) with some missing functionality.

# WARNING: URI is not a local file
**Beware**: Inside understand.ai we will hand cloud paths as URIs. So using the string of a path to open it will fail in these cases!
E.g. Do **not** do things like this:
```python
from uai_pre_import_transform_interface import PreImportTransformInterface, URI
from PIL import Image

class PreImportTransformer(PreImportTransformInterface):
    def transform(self, input_path: URI, output_path: URI):
        path_to_image = input_path / "images" / "00001.png"
        with Image.open(str(path_to_image)) as im:  # This will fail if input path is "gs://dataset/clip1/"
            im.show()
```
instead you could do
```python
from uai_pre_import_transform_interface import PreImportTransformInterface, URI
from PIL import Image
from tempfile import NamedTemporaryFile

class PreImportTransformer(PreImportTransformInterface):
    def transform(self, input_path: URI, output_path: URI):
        path_to_image = input_path / "images" / "00001.png"
        
        # example for when your method takes readable bytes
        with Image.open(path_to_image.open("rb")) as im:
            im.show()

        # example for when your method needs just a path to the file
        with NamedTemporaryFile() as tmp:
            tmp.write(path_to_image.open("rb").read())
            Image.open(tmp.name)
```

**Unit tests do not catch this, unfortunately**. One idea to be more save against this could be to not use pathlib.Path directly for debugging but to instead extend path with an implementation that raises an error on usage of `__str__`.
```python
from pathlib import Path

class DebuPath(Path):
    def __str__(self):
        raise Exception("it is not a good idea to use strings for paths for anything but logging as these paths could point to remote resources.")
```

# Implementation
Every implementation should provide a python package named by you. Let's use `package_name` as an example. From this package the following import has to work:
```python
from package_name import PreImportTransformer
```
This should give your implementation of the interface. To achieve this the `__init__.py` oyour package should contain something like this (depending on how you name things):
```python
from .my_interface_implementation import PreImportTransformer
__all__: Sequence[str] = ["PreImportTransformer"]
```

This is how we will automatically bind your library into our system. ![img.png](package_architecture.png)
