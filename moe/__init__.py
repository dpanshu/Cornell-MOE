# -*- coding: utf-8 -*-

#: Following the versioning system at http://semver.org/
#: See also docs/contributing.rst, section ``Versioning``
#: MAJOR: incremented for incompatible API changes
MAJOR = 0
#: MINOR: incremented for adding functionality in a backwards-compatible manner
MINOR = 2
#: PATCH: incremented for backward-compatible bug fixes and minor capability improvements
PATCH = 2
#: Latest release version of MOE
__version__ = "{0:d}.{1:d}.{2:d}".format(MAJOR, MINOR, PATCH)
