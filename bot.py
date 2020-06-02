import requests
import json
def hasSixSeasons(id):
    querystring = {"i": id,"type":"series","r":"json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    info = response.json()
    return info["totalSeasons"] == '6';

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

# querystring = {"page":"1","r":"json","s":"Avengers Endgame"}
f = open("api-key.txt", "r")
key = f.readline().strip()
f.close()
headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': key
    }
# id = "tt0175058" # powerpuff girls yes
# id = "tt1439629" # community yes
# id = "tt0804503" # mad men no
id = "tt4158110" # mr robot no
print(hasSixSeasons(id))
# querystring = {"i": id,"type":"series","r":"json"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# f = open("response.json","w")
# # print(response.json())
# f.write(response.text)
# f.close()
