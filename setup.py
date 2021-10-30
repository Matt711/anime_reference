# Author: Matt Murray
# Description:

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='anime_reference',
      version='0.0.10',
      description='A reference package for all things anime.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Matt711/anime_reference',
      author='Matt Murray',
      author_email='matthewmurray711@gmail.com',
      license='MIT',
      packages=['anime_reference'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=[
          'beautifulsoup4==4.9.3',
          'requests==2.25.1',
          'pandas==1.2.4',
          'lxml==4.6.3',
          'html5lib==1.1'
      ],
      keywords=[
          "fandom anime",
          "manga",
          "data mining",
          "anime",
          "anime reference",
          "manga reference"
      ]
      )
