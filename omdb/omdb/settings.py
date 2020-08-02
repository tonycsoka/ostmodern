import os
from pathlib import Path
import functools

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OMDB_API_KEY = os.getenv("OMDB_API_KEY", "")


def omdbkeyrequired(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if OMDB_API_KEY == "":
            raise Exception("OMDB_API_KEY must be set in env")
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator
