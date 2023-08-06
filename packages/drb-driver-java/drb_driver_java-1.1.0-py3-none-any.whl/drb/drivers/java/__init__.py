from . import _version

__version__ = _version.get_versions()['version']

from .drb_driver_java_node import DrbJavaBaseNode, DrbJavaNode

del _version

__all__ = [
    'DrbJavaNode',
    'DrbJavaBaseNode',
]
