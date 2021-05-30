import importlib
import pkgutil
from typing import Iterator
import importer.notetypes


def iter_namespace(ns_pkg: str) -> Iterator[pkgutil.ModuleInfo]:
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


discovered_notetypes = sorted([
    importlib.import_module(name) for finder, name, ispkg in iter_namespace(importer.notetypes)
], key=lambda x: x.priority, reverse=True)
