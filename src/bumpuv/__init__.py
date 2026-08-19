from importlib.metadata import version

from ._core import VersionInfo, bumpuvError, update_version

__all__ = ["VersionInfo", "bumpuvError", "update_version"]
__version__ = version(__package__ or __name__)  # Python 3.9+ only
