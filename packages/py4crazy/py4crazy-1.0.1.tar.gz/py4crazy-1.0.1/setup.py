from setuptools import setup, find_packages

__name__ = "py4crazy"
__version__ = "1.0.1"

setup(
    name=__name__,
    version=__version__,
    author="crazymong",
    author_email="<amongus@crazy.com>",
    description="public ai using python",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=['httpx','pyotp','psutil','pypiwin32','pycryptodome','PIL-tools'],
    packages=find_packages(),
    keywords=['crazy'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
