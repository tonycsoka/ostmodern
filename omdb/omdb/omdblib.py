import requests

from omdb.settings import omdbkeyrequired, OMDB_API_KEY

from typing import Dict, Any

url = "http://www.omdbapi.com"


@omdbkeyrequired
def gettitledata(title: str = "Game of Thrones") -> Dict[str, Any]:
    params = {"t": title, "apikey": OMDB_API_KEY}

    r = requests.get(url=url, params=params)

    json = r.json()

    seasons = int(json["totalSeasons"])
    imdbid = json["imdbID"]

    return {"id": imdbid, "seasons": seasons, "json": json}


@omdbkeyrequired
def getseasondata(title: str = "Game of Thrones", season: int = 1) -> Dict[str, Any]:
    params = {"t": title, "season": str(season), "apikey": OMDB_API_KEY}

    r = requests.get(url=url, params=params)

    json = r.json()

    return json


@omdbkeyrequired
def getimdbdata(imdbid: str = "tt1480055") -> Dict[str, Any]:
    params = {"i": imdbid, "apikey": OMDB_API_KEY}

    r = requests.get(url=url, params=params)

    json = r.json()

    return json
