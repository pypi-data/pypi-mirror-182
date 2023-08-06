from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="debategpt",
    description="Train and use DebateGPT, a language model designed to simulate debates.",
    author="paulbricman",
    version="0.0.1",
    packages=["debategpt", "debategpt.training", "debategpt.inference"],
    install_requires=requirements,
)
