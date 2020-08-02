from omdb.omdblib import getimdbdata, getseasondata, gettitledata

titledata = gettitledata()

for i in range(titledata["seasons"]):
    season = i + 1
    seasondata = getseasondata(season=season)

    for j in seasondata["Episodes"]:
        imdbid = j["imdbID"]

        episodedata = getimdbdata(imdbid=imdbid)

        print(episodedata)
