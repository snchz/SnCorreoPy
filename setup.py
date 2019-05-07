from setuptools import setup, find_packages
from codecs import open
import os, ast


with open('README.rst', encoding='utf-8') as f:
	descripcion_larga=f.read()

def extract_values(source_file, desired_vars):
    with open(source_file) as f:
        for line in f:
            if any(line.startswith(var) for var in desired_vars):
                parsed = ast.parse(line).body[0]
                yield parsed.targets[0].id, parsed.value.s

package_name='sncorreopy'
filename = os.path.join(package_name, '__init__.py')
metadata_names = '__author__', '__version__','__doc__','__license__'
values = dict(extract_values(filename, metadata_names))

setup(
	name='sncorreopy',
	version=values['__version__'],
	description=values['__doc__'],
	long_description=descripcion_larga,
	url='',
	author=values['__author__'],
	author_email='',
	license=values['__license__'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Utilities',
		'License :: GNU General Public License v3',
		'Programming Language :: Python :: 3',
		'Enviromment :: Console'
	],
	keywords='correo electronico mail',
	packages=find_packages(),
)
