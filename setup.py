from setuptools import setup, find_packages
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(name="shopping_cart",
      version='1.0.0',
      description='Shopping cart implementation in python.',
      author='Abhilash Kadhane',
      install_requires=install_requires,
      packages=find_packages())
