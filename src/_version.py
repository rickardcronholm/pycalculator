"""${SHORT_DESCRIPTION}"""
import re

__version__ = "0.0.1"
__version_info__ = tuple(
    re.match(r"(\d+\.\d+\.\d+).*", __version__).group(1).split(".")
)
