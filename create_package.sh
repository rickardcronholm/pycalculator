# ----------------------------------------------------------------------------------------
#
#   Copyright 2018, Spectronic Medical AB, Helsingborg, Sweden
#
#   All rights reserved. File may not be used, copied, reviewed, executed or
#   otherwise utilized for any purpose without prior written approval from
#   Spectronic Medical AB.
#
# ----------------------------------------------------------------------------------------

# Collect INFORMATION
year=$(date +'%Y')
read -p "PACKAGE NAME: " PACKAGE_NAME
read -p "SHORT DESCRIPTION: " SHORT_DESCRIPTION

# PUSH to new repo
repo_name="py${PACKAGE_NAME}.git"
git push --mirror ${repo_name}
