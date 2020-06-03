import requests
import json

#maybe a bot that tweets the top 10 imdb movies starting from 1980?
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

def clown(year):
    querystring ={ "page": "1", "r":"json","y":str(year),"type":"movie","s":"clown"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    info = response.json()
    # f = open("response.json", "w")
    # f.write(response.text);
    if "Search" in info:
        for item in info["Search"]:
            poster = item["Poster"]
            title = item["Title"]
            if poster != "N/A":
                result = {"title":title,"poster": poster}
                return result
        result = {"title":title}
        return result

#given the name of a tv show return whether it has a movie
# maybe if 1 of the creators directed it
def hasMovie(name):
    pass
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

print(clown(1970))
# querystring ={ "page": "1", "r":"json","y":"1980","type":"movie","s":"clown"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# f = open("response.json", "w")
# f.write(response.text);
