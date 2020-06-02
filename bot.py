import requests
import json
def getId(name):
    querystring ={ "page": "1", "r":"json","s": name}
    response = requests.request("GET", url, headers=headers, params=querystring)
    info = response.json()
    # return id of the first result shown
    return info["Search"][0]["imdbID"]
def hasSixSeasons(name):
    id = getId(name)
    querystring = {"i": id,"type":"series","r":"json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    info = response.json()
    return info["totalSeasons"] == '6';
def test():
    assert(hasSixSeasons("community"))
    assert(hasSixSeasons("the powerpuff girls"))
    assert(not hasSixSeasons("mad men"))
    assert(not hasSixSeasons("mr robot"))

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

f = open("api-key.txt", "r")
key = f.readline().strip()
f.close()
headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': key
    }
