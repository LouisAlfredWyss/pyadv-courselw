"""Package description."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-courselw")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Louis Wyss"
__email__ = "louis.wyss@insel.ch"
