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
cwd=$PWD
year=$(date +'%Y')
read -p "LOCAL PATH TO NEW PACKAGE: " PTH
read -p "PACKAGE NAME: " PACKAGE_NAME
read -p "SHORT DESCRIPTION: " SHORT_DESCRIPTION

# PUSH to new repo
repo_path="/shared/admin/git-repo"
repo_name="py${PACKAGE_NAME}"
git clone --bare "${repo_path}/clean_package.git"
cd clean_package.git
git init --bare "${repo_path}/${repo_name}.git"
git push --mirror "${repo_path}/${repo_name}.git"

# clone new repo
cd $PTH
git clone "${repo_path}/${repo_name}.git"
cd ${repo_name}

# Start modyfing
# YEAR
sed -i 's:$YYYY:'"${year}"':g' copyright
# PREPEND copyright
mkdir -p tmp/src
for item in README.md setup.py src/_version.py src/__init__.py src/__main__.py
do
    cat "copyright" > tmp/$item
    cat $item >> tmp/$item
    mv tmp/$item $item
done
rmdir tmp/src
rmdir tmp
# SHORT DESCRIPTION
sed -i 's:${SHORT_DESCRIPTION}:'"${SHORT_DESCRIPTION}"':g' */*
sed -i 's:${SHORT_DESCRIPTION}:'"${SHORT_DESCRIPTION}"':g' *
# PACKAGE NAME
sed -i 's:${PACKAGE_NAME}:'"${PACKAGE_NAME}"':g' */*
sed -i 's:${PACKAGE_NAME}:'"${PACKAGE_NAME}"':g' *
# rename src
mv src ${PACKAGE_NAME}

# remove files
for item in copyright create_package.sh
do
    rm $item
done
# copy .gitignore
cp $cwd/.gitignore .

# Initial commit
git add *
git commit -m "Initial commit"
git push

# back to where I came from
cd $cwd
rm -rf clean_package.git
