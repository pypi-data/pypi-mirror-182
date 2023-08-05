import versioneer
from setuptools import find_namespace_packages, setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.readlines()

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="drb-driver-zarr",
    packages=find_namespace_packages(include=["drb.*"]),
    description="DRB Zarr driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GAEL Systems",
    author_email="drb-python@gael.fr",
    url="https://gitlab.com/drb-python/impl/zarr",
    install_requires=REQUIREMENTS,
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "drb.driver": "zarr = drb.drivers.zarr:DrbZarrFactory",
        "drb.topic": "zarr = drb.topics.zarr",
    },
    package_data={"drb.topics.zarr": ["cortex.yml"]},
    version=versioneer.get_version(),
    data_files=[(".", ["requirements.txt"])],
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        "Documentation": "https://drb-python.gitlab.io/impl/zarr",
        "Source": "https://gitlab.com/drb-python/impl/zarr",
    },
)
