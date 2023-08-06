from setuptools import setup, find_packages
import os

VERSION = '0.0.7'
DESCRIPTION = 'Easily downlaod file from cow transfer'

setup(
    name="cow_download",
    version=VERSION,
    author="txb",
    author_email="txb.sdn@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['DownloadKit', 'requests'],
    keywords=['python', 'DownloadKit', 'cow_download'],
    entry_points={
    'console_scripts': [
        'cow = cow_download.main:main'
    ]
    },
    license="MIT",
    url="https://github.com/txbhandsome/cow_download.git",
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)