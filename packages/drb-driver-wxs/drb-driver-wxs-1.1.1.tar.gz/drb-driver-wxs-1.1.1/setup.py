import versioneer
from setuptools import find_namespace_packages, setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.readlines()

with open("README.md") as f:
    long_description = f.read()


setup(
    name="drb-driver-wxs",
    packages=find_namespace_packages(include=["drb.*"]),
    description="DRB WXS OGC Service driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GAEL Systems",
    author_email="drb-python@gael.fr",
    url="https://gitlab.com/drb-python/impl/wXs",
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    data_files=[(".", ["requirements.txt"])],
)
