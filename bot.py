import requests
import json
import tweepy
from os import environ
import time


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
    result = {}
    if "Search" in info:
        for item in info["Search"]:
            poster = item["Poster"]
            title = item["Title"]
            id = item["imdbID"]
            if poster != "N/A":
                result["title"] = title
                result["poster"] = poster
                querystring = {"i": id,"type":"movie","r":"json","plot":"short"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                info = response.json()
                result["director"] =  info["Director"]
                result["release-date"] = info["Released"]
                return result
        result["title"] = title
        querystring = {"i": id,"type":"movie","r":"json","plot":"short"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        info = response.json()
        result["director"] =  info["Director"]
        result["release-date"] = info["Released"]
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

# f = open("api-key.txt", "r")
# key = f.readline().strip()
# f.close()
headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': environ["imdb-key"]
    }

# twitter_credentials ={}
# with open("clown-api-keys.json") as json_file:
#     twitter_credentials = json.load(json_file)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(environ["api-key"],
    environ["api-key-secret"])
auth.set_access_token(environ["access-token"],
    environ["access-token-secret"])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
# api.update_status("Test tweet from Tweepy Python")

def post_clown(year):
    movie = clown(year)
    if movie is not None:
        title = movie["title"]
        director = movie["director"]
        release_date = movie["release-date"]
        poster = ""
        media = None
        if "poster" in movie:
            poster = movie["poster"]
            response = requests.request("GET",poster)
            with open('poster.png', 'wb') as f:
                f.write(response.content)
            media = api.media_upload("poster.png")
        tweet_format = "%s (%s)\nDirected by %s"
        tweet = tweet_format % (title,year,director)
        # tweet_format = "%s (%s)"
        # tweet = tweet_format % (title,str(year))
        if media is not None:
            post_result = api.update_status(status=tweet, media_ids=[media.media_id])
        else:
            post_result = api.update_status(tweet)
year = 1976
INTERVAL = 60 * 60 * 4   # tweet every 4 hours
while True:
    print("posting clown movie from %d" % year)
    post_clown(year)
    year += 1
    if year > 2020:
        year = 1976
    time.sleep(INTERVAL)

# querystring ={ "page": "1", "r":"json","y":"1980","type":"movie","s":"clown"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# f = open("response.json", "w")
# f.write(response.text);
