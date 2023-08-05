from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="orchard_client",
    version="1.0.0",
    description="Orchard api client",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="",
    author="Akorlie Edward Tsastu",
    author_email="edward@appsnmobilesolutions.com",
    license="MIT",
    classifiers=classifiers,
    keywords="orchard_client",
    packages=find_packages(),
    install_requires=["requests", "json", "hmac", "hashlib"],
)