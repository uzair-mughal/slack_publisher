from distutils.core import setup
from setuptools import find_packages, setup


setup(
    name="slack_publisher",
    packages=find_packages(),
    version="0.0.1",
    license="MIT",
    description="",
    author="Uzair Ahmed Mughal",
    author_email="uzam.dev@gmail.com",
    url="",
    download_url="",
    keywords=["Slack"],
    install_requires=["slack_sdk"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
