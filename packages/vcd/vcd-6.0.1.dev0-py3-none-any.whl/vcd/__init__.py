"""
VCD (Video Content Description) library

Project website: http://vcd.vicomtech.org

Copyright (C) 2022, Vicomtech (http://www.vicomtech.es/),
(Spain) all rights reserved.

VCD is a Python library to create and manage OpenLABEL content.
VCD is distributed under MIT License. See LICENSE.

"""

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")
