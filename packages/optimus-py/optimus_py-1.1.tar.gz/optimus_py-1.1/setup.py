from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='optimus_py',
    version='1.1',
    author='Kavin Bharathi',
    author_email='r.m.kavinbharathi@gmail.com',
    description='Code optimization documentation & timing module',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/kavinbharathii/",
    packages = find_packages(),
    install_requires=[
        requirements
    ],
    python_requires='>=3.5',
)