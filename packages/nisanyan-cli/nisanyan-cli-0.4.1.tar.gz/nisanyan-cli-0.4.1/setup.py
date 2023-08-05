from setuptools import setup
from nisanyan_cli import __version__ as VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

DESCRIPTION = (
    "CLI tool for Turkish etymological dictionary, nisanyansozluk.com (nis <word>)"
)

setup(
    name="nisanyan-cli",
    version=VERSION,
    url="https://github.com/agmmnn/nisanyan-cli",
    project_urls={
        "Changelog": "https://github.com/agmmnn/nisanyan-cli/releases",
        "Source": "https://github.com/agmmnn/nisanyan-cli",
    },
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["nisanyan_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"nisanyan_cli": ["nisanyan_cli/*"]},
    python_requires=">=3.6.3",
    entry_points={"console_scripts": ["nis = nisanyan_cli.__main__:cli"]},
)
