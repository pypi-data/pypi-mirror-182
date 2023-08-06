"""
Type this in terminal to upgrade the package.
Step-1
    remove unuse directories
Step-2
    input command
    >> python setup.py sdist bdist_wheel
    >> twine upload dist/*
"""
from setuptools import find_packages, setup

setup(name="handyplot",
      version="0.3.6",
      description="Test.",
      author="Hong Peng",
      python_requires=">=3.8.0",
      url="https://github.com/minho-hong/handyplot.git",
      package_data={},
      packages=find_packages(),
      install_requires=["matplotlib", "numpy", "vtk"],
      license="GPL")