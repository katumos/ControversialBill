import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
   name = "Controversial Bill",
   version = "0.0.1",
   description = ("A Django website to facilitate collaborative editing of legislations"),
   license = "Apache",
   url = "http://www.controversialbill.org",
   packages = ["legislation_editor"],
   long_description = read('README'),
   classifiers = [
      "Development Status :: Alpha",
      "Topic :: Webapp"
      "License :: Apache",
   ],
   install_requires = [
      "Django==1.3.1",
   ]
)
   

