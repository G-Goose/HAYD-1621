from setuptools import setup, find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='hayd1621',
      description="Setup How Are You Doing Today?",
      packages=find_packages(),
      install_requires=requirements)
