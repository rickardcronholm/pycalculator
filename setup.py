# ----------------------------------------------------------------------------------------
#
#   Copyright 2018, Spectronic Medical AB, Helsingborg, Sweden
#
#   All rights reserved. File may not be used, copied, reviewed, executed or
#   otherwise utilized for any purpose without prior written approval from
#   Spectronic Medical AB.
#
# ----------------------------------------------------------------------------------------

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

# get __version__ from _version.py
base_dir = os.path.dirname(os.path.realpath(__file__))
ver_file = os.path.join(base_dir, "calculator", '_version.py')
with open(ver_file) as f:
    exec(f.read())

def data_files_inventory():
    data_files = []
    data_roots = ["calculator/data"]
    for data_root in data_roots:
        for root, subfolder, files in os.walk(data_root):
            files = [x.replace("calculator/", "") for x in glob(root + "/*")
                     if not os.path.isdir(x)]
            data_files = data_files + files
    return data_files


setup(
    name = "calculator",
    version = __version__,

    author = "Spectronic Medical AB",
    author_email = "support@spectronic.se",

    description = "Basic Python calculator",
    long_description = long_description,
    long_description_content_type= " text/markdown",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=find_packages(exclude=["tests"]),


    package_data = {"calculator": data_files_inventory()},


    python_requires='>=3',
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires = [

    ],

    classifiers = [

    ],


    zip_safe = False,
)
