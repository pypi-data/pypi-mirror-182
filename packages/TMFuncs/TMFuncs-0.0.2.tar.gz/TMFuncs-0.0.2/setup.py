from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='TMFuncs',
      version='0.0.2',
      description='Databricks common functions, written by TrueMetrics.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://www.truemetrics.cn/',
      author='TSO',
      author_email='tlsong@truemetrics.cn',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3.9",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )