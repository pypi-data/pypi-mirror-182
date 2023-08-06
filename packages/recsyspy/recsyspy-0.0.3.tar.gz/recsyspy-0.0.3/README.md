# RecSysPy | Python Recommender System Package

![version](https://img.shields.io/badge/version-0.0.3-blue)

Python package calculating recommendations from implicit feedback.

# Development

## Project Setup

Project Setup forked from GitHub Repository [PythonExampleProject](https://github.com/Coding-Crashkurse/PythonExampleProject) (see tutorial in [YouTube](https://www.youtube.com/watch?v=3QvUqHIglmo)).

# Testing

Before pushing commits to `develop` branch run `tox` from the project root.

> TODO: This needs to be automatd and pushed to a GitHub Action

# Build & Distribution

## TestPyPI

A GitHub Action is in place that builds and publishes to **TestPyPI** whenever a commit is **pushed** to the `develop` branch.

For building and publishing to **TestPyPI** (not recommended) see official [PyPI Docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```cmd
py -m build
py -m twine upload --repository testpypi dist/*
```

## PyPI

Another GitHub Action is in place on **pull requests** on the `main` branch. The Python Package will be build and published to **PyPI**.
