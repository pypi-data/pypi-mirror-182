
# Copyright (c) 2001-present Guangzhou ZHIYUAN Electronics Co., Ltd..
# All rights reserved.

import os
import platform
import sys

REQUIRED_PYTHON_VERSION = "3.7"
if sys.version[:3] != REQUIRED_PYTHON_VERSION:
    raise ValueError('this axio-cli distribute only work with python{} , not compatible with this python {}'.format(REQUIRED_PYTHON_VERSION, sys.version))


PY2 = sys.version[0] == '2'

pysite_axio = os.environ.get('AXIOPYSITEDIR')
print(sys.path)
if pysite_axio:
    sys.path.insert(0, pysite_axio)

from setuptools import find_packages, setup

def make_datafiles(tgt_dir, src_dir):
    files = []
    data_files = []
    for f in os.listdir(src_dir):
        tgt_f = os.path.join(tgt_dir, f)
        src_f = os.path.join(src_dir, f)
        if os.path.isdir(src_f):
            data_files.extend(make_datafiles(tgt_f, src_f))
        else:
            if src_f.endswith('.pyc'):
                continue
            files.append(src_f)
    data_files.append((tgt_dir, files),)
    return data_files

def gen_datafiles(tgt_dir, src_dir):
    excludes = ["pip", "wheel", "easy_install.py", ]
    files = []
    data_files = []
    for f in os.listdir(src_dir):
        if f in excludes:
            continue
        if any(map(lambda ex: ex+'-' in f, excludes)):
            continue
        tgt_f = os.path.join(tgt_dir, f)
        src_f = os.path.join(src_dir, f)
        if os.path.isdir(src_f):
            data_files.extend(make_datafiles(tgt_f, src_f))
        else:
            if src_f.endswith('.pyc'):
                continue
            files.append(src_f)
    data_files.append((tgt_dir, files),)
    return data_files

site_dir = "Lib/site-packages/" if platform.system().lower() == 'windows' else "lib/python2.7/site-packages/" if PY2 else "lib/python3.7/site-packages/"
data_files = gen_datafiles(site_dir+'axiolib/pysite-axio', 'axiolib/pysite-axio')
builders = gen_datafiles(site_dir+'axiolib/builders', 'axiolib/builders')
managers = gen_datafiles(site_dir+'axiolib/managers', 'axiolib/managers')
toolchains = gen_datafiles(site_dir+'axiolib/toolchains', 'axiolib/toolchains')
packages = gen_datafiles(site_dir+'axiolib/packages', 'axiolib/packages')
data_files += builders + managers + toolchains + packages

setup(
    name="axio-cli",
    version= "1.1.0a101",
    title = "axio-cli",
    description="axio client command line tool",
    # long_description=open("README.rst").read(),
    author="zlg",
    # author_email="support@zlg.cn",
    # url=__url__,
    # license=__license__,
    packages= find_packages(),
    package_data={
      'axiolib': ['axbuilder/*',
                   'axbuilder/tools/*',
                   'axbuilder/tools/packagers/*',
                   'bin/*',
                   'data/*',
                   'data/locales/*/*/*',
                   'package.json',
                   'app_profile.json',
                   'CHANGELOG.rst'],
    },

    data_files= data_files,
    # install_requires=[
    #     'Click',
    #     'python-winscp',
    #     'semantic_version',
    #     'toml'
    # ],

    entry_points='''
        [console_scripts]
        axio=axiolib.cli_axio_launcher:main
    ''',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Compilers"
    ],
)