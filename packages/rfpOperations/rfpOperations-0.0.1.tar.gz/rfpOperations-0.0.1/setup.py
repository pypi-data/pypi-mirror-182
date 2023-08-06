from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'This package includes stuff for rental-flat-project'
LONG_DESCRIPTION = 'Scraper, Identifier and some operations on Db'

setup(
        name="rfpOperations",
        version=VERSION,
        author="H.B.",
        author_email="<han.kagan.b@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package
	# ??? do you need any

        keywords=['python', 'rfp package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)

