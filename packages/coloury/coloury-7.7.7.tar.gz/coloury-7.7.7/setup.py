from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 3 - Alpha",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9"
]
 
setup(
  name="coloury",
  version="7.7.7",
  description="Make your ASCII art beautiful!",
  long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
  url="https://github.com/CodeIntelligenceAgency",  
  author="Cyanraze",
  author_email="cyan@cia.works",
  license="MIT", 
  keywords="coloury", 
  classifiers=classifiers,
  packages=["coloury"]
)