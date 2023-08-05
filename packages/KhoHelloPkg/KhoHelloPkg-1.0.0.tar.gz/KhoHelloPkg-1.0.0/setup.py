
from setuptools import setup, find_packages


# Get the long description from the README file
long_description = 'Testing the packaging process'


setup(
    name="KhoHelloPkg",
    version="1.0.0", 
    description="A sample Python Hello World",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Khobeib Developer",
    author_email="author@example.com",
    classifiers=[ 
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)