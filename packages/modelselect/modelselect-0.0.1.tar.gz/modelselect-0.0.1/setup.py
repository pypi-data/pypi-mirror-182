
from setuptools import setup, find_packages

from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'A package helps select independent variables for traditional linear regression models'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="modelselect",
    version=VERSION,
    author="Shouke Wei",
    author_email="shouke.wei@gmail.com",
    license='MIT License',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url = 'https://github.com/shoukewei/modelselect',
    project_url = 'https://github.com/shoukewei/modelselect',
    Documentation = 'https://github.com/shoukewei/modelselect/blob/main/docs/example.ipynb',
    packages=find_packages(),
    install_requires=['pandas','statsmodels'],
    keywords=['python', 'linear regression', 'statsmodels','model improvement', 'select variables','insignificant','multicollinearity'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)