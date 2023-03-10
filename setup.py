import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        f = r':[a-z]+:`~?(.*?)`'
        return re.sub(text_type(f), text_type(r'``\1``'), fd.read())


setup(
    name="example-svc",
    version="0.1.0",
    url="https://github.com/claick-oliveira/k8s-gateway-api",
    license='MIT',
    author="Claick Oliveira",
    author_email="@",
    description="Example service.",
    long_description=read("README.md"),
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
