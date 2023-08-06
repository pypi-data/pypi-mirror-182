from importlib import resources

from jubeatools.formats import LOADERS
from jubeatools.formats.guess import guess_format


def load_test_file(package: resources.Package, file: str) -> None:
    with resources.as_file(resources.files(package) / file) as p:
        format_ = guess_format(p)
        loader = LOADERS[format_]
        _ = loader(p)
