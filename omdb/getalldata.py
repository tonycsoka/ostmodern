from pathlib import Path
import json
from omdb.omdblib import getimdbdata, getseasondata, gettitledata
from omdb.settings import DATA_DIR


def writejson(fname: str, data: dict):
    jdata = json.dumps(data)
    f = open(fname, "w")
    f.write(jdata)
    f.close()


Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

titledata = gettitledata()

fname = str(Path(DATA_DIR, "titledata.json"))

writejson(fname, titledata["json"])

for i in range(titledata["seasons"]):
    season = i + 1
    seasondata = getseasondata(season=season)

    fname = str(Path(DATA_DIR, "seasondata-{}.json".format(season)))

    writejson(fname, seasondata)

    for j in seasondata["Episodes"]:
        imdbid = j["imdbID"]

        episodedata = getimdbdata(imdbid=imdbid)

        fname = str(Path(DATA_DIR, "episodedata-{}.json".format(imdbid)))

        writejson(fname, episodedata)
