
from setuptools import setup, find_packages

from pathlib import Path

VERSION = '0.0.2'
DESCRIPTION = 'A descriptive statistics package'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="descripstats",
    version=VERSION,
    author="Shouke Wei",
    author_email="shouke.wei@gmail.com",
    license='MIT License',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url = 'https://github.com/shoukewei/descripstats',
    project_url = 'https://github.com/shoukewei/descripstats',
    Documentation = 'https://github.com/shoukewei/descripstats/blob/main/docs/example.ipynb',
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python', 'descriptive statistics', 'more measures', 'pandas describe','pandas dataframe'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)