"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name="local_environment",
    version="1.0.0",
    private=True,
    description="Landa's Local Environment Management Library",
    author="Amit Assaraf",
    author_email="amit@landa.app",
    license="MIT",
    keywords="setuptools development",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    install_requires=[
        i.strip()
        for i in open("requirements.txt").readlines()
        if not i.strip().startswith("-e")
    ],
)
