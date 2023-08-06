# -*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
# from Cython.Build import cythonize

with open('photoutils/version.py', 'r') as f:
	x = f.read()
	y = x[x.index("'")+1:]
	version = y[:y.index("'")]
print(f'{version=}')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


description = "photoutils is contains a set of photo utilitiesi and function"
author = "yumoqing"
email = "yumoqing@icloud.com"

package_data = {
	"photoutils":[
		'imgs/*.png', 
		'imgs/*.atlas', 
		'imgs/*.gif'
	]
}
setup(
    name="photoutils",
	# ext_modules= cythonize( [ ]),
	ext_modules= [],
    version=version,
    description=description,
	long_description=long_description,
	long_description_content_type="text/markdown",
    author=author,
    author_email=email,
    install_requires=[
    ],
    packages=[
		'photoutils'
	],
    package_data=package_data,
    keywords = [
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
	platforms= 'any'
)
