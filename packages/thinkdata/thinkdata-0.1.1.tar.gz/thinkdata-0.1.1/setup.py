from setuptools import find_packages, setup

setup(
    name="thinkdata",
    version="0.1.1",
    author="brendon.lin",
    author_email="brendon.lin@outlook.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pandas>=1.3.5",
        "networkx>=2.6.3",
        "matplotlib>=3.5.2"
    ],
    description="Data analysis tool for Metric System",
)
