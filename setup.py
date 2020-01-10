import os
import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="py_auth_header_parser",
    version="1.0.0",
    author="Chrys Gonsalves",
    author_email="cgons@pcxchange.ca",
    description="Small and simple Python library to parse JWT tokens embedded in http auth. headers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgons/py-auth-header-parser",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            "wheel",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
