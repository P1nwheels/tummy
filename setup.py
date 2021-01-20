from setuptools import setup, find_packages


def requires():
    with open("requirements.txt", "r") as reqs:
        return [line.strip() for line in reqs.readlines()]


setup(
    name="tummy",
    author="Pinwheel",
    author_email="redacted",
    version="1.0.0",
    description="A collection of CLI tools for myself :)",
    url="https://github.com/P1nwheels/tummy",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires(),
    entry_points="""
        [console_scripts]
        tummy=tummy.main:main
    """
)