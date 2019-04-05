"""
molssi_devops_uf
sample project for molssi workshop
"""

# Add imports here
from .molssi_math import *
from .string_util import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
