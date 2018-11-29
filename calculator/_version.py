# ----------------------------------------------------------------------------------------
#
#   Copyright 2018, Spectronic Medical AB, Helsingborg, Sweden
#
#   All rights reserved. File may not be used, copied, reviewed, executed or
#   otherwise utilized for any purpose without prior written approval from
#   Spectronic Medical AB.
#
# ----------------------------------------------------------------------------------------

"""Basic Python calculator"""
import re

__version__ = "0.0.1"
__version_info__ = tuple(
    re.match(r"(\d+\.\d+\.\d+).*", __version__).group(1).split(".")
)
