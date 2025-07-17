from setuptools import setup, find_packages 

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Anime_recommender",
    version="0.1",
    author="MANAS KULKARNI",
    install_requires=requirements,
    packages=find_packages(),)

