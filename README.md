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

## Downloading data

To download all the data run the following

```zsh
$> cd omdb
$> python getalldata.py
```

This will write the downloaded files to an output directory under `omdb`, as specified by the env var `DATA_DIR`, which defaults to `data`.

## Schema

The options schema wise are to keep the data in json format and store in a document database, turning the data into a relational schema, or storing the data against a key in a key-value database.

### Document Store

In terms of storing the data as downloaded, this is by far the easiest option, as the data can be stored as is without a though to structure.  The work comes in parsing the data for consumption by the API.  The benefits of this are that we are imune to any changes upstream in tems of grabbing data, which would be important if at any stage we would want to store a history of data (for instance, to track changes in ratings).  The downside, is that all the processing to return only the data the end user is interested in happens in the API, so performance will take a small hit.

### Key Value Store

A key value store is almost the same as a document store in terms of ease, however there is a small risk that the document structure could change such that extracting the key from each document would throw an exception.

### Relational Database

A relation database would have the benefit of being structured in such a way as to only store the information needed for the end users, however and change in the upstream system could result in serious downtimes, or loss of data.  When it comes to storing extra information (for example comments), then a relational database makes sense, however this does not rule out using a hybrid system, for example, document store for `static` data, and a relationl db for `comments`

Taking this a step further, a document store can be used for the raw static data, which is transformed and cached (either lazily or on a timed trigger) to a key-value store.
