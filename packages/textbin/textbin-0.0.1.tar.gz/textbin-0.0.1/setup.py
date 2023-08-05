from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'textbin packge'
LONG_DESCRIPTION = 'A package that allows to convert text to binary and binary to text.'

# Setting up
setup(
    name="textbin",
    version=VERSION,
    author="Comon (Collins Omondi)",
    author_email="<comon928@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['binary', 'text' ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

