from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'This script computes the basin entropy of a computed basin of attraction on a regular grid.The function return the basin entropy and the boundary basin entropy'
LONG_DESCRIPTION = 'This algorithm computes the basin entropy of a computed basin of attraction on a regular grid.The function return the basin entropy and the boundary basin entropy. [A. Daza, A. Wagemakers, B. Georgeot, D. Guéry-Odelin and M. A. F. Sanjuán, Basin entropy: a new tool to analyze uncertainty in dynamical systems, Sci. Rep., 6, 31416, (2016).]' 

# Setting up
setup(
    name="basinentropycalc",
    version=VERSION,
    author="Oliveira, Jonas",
    author_email="<jonasferoliveira.ufg@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'basins', 'chaos', 'entropy', 'fractals','dynamical systems','EDOs', 'chaotic maps'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
