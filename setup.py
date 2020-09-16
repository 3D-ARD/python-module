from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, '3dard', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='3dard',
    version=version['__version__'],
    description=('Python module to query an fetch the 3D-ARD project.'),
    long_description=long_description,
    author='Nicolas Mellado',
    author_email='nmellado0@gmail.com',
    url='https://github.com/3D-ARD/python-module',
    license='MPL-2.0',
    packages=['3dard'],
#   no dependencies in this example
#   install_requires=[
#       'dependency==1.2.3',
#   ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
