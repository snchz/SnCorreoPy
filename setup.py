from setuptools import setup, find_packages
from codecs import open
import sncorreopi


with open('README.rst', encoding='utf-8') as f:
	descripcion_larga=f.read()

setup(
	name='sncorreopy',
	version=sncorreopi.__version__,
	description=sncorreopi.__doc__.strip(),
	long_description=descripcion_larga,
	url='',
	author=sncorreopi.__author__,
	author_email='',
	license=sncorreopi.__license__,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Utilities',
		'License :: GNU General Public License v3',
		'Programming Language :: Python :: 3',
		'Enviromment :: Console'
	],
	keywords='correo electronico mail'
	packages=find_packages(),
)