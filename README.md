# Introduction
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub issues](https://img.shields.io/github/issues/tonycsoka/ostmodern)
![Python Version](https://img.shields.io/badge/python-3.8-blue)


For an overview of this coding task see the [instrucions provided by OST Modern](README-OSTModern.md)

## Instructions

This was developed using python 3.8.2, so if coding locally, it is recommended to install this (preferably using a python version manager e.g. pyenv).

Once you've set up 3.8.2 as the shells python (for instructions see the [pyenv documentation](https://github.com/pyenv/pyenv/blob/master/README.md)), install a virtual environment in the local directory, and activate

```zsh
$> python -m venv venv
$> source venv/bin/activate
```

Next, install any required packages using pip (and install pre-commit hooks)

For development use

```zsh
$> pip install -r requirements-dev.txt
$> pre-commit install
```

and for production

```zsh
$> pip install -r requirements.txt
```

## Running

To download all the data run the following

```zsh
$> cd omdb
$> python getalldata.py
```
