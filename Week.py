import re
import certifi
import urllib3, json
from Game import *

class Week():
    """represents a week with Games"""
    baseURL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=2023&seasontype=2&week=16"

    def __init__(self, year, week):
        self.year = year
        self.week = week

        # replace year/week in base URL to be used with specific values
        self.url = re.sub("dates=(\d{4})", f"year={str(self.year)}", self.baseURL)
        self.url = re.sub("week=(\d+)", f"week={str(self.week)}", self.url)
        # print(self.url)

        # create empty list of games; games will be appended in readData() function
        self.games = []

    def readData(self):

        http = urllib3.PoolManager(
            cert_reqs="CERT_REQUIRED",
            ca_certs=certifi.where()
        )

        resp = http.request("GET", self.url)
        data = resp.json()

        self.events = data["events"]
        # print(self.events)
        for event in self.events:
            week = event["week"]
            uid = event["uid"]
            gamedate = event["date"]
            competitions = event["competitions"]
            # print(event["id"], event["shortName"])
            for competition in competitions:
                venue = competition["venue"]["fullName"]
                competitors = competition["competitors"]
                for competitor in competitors:
                    team = competitor["team"]
                    if competitor["homeAway"] == "home":
                        home_abbr = team["abbreviation"]
                        home_score = int(competitor["score"])
                    if competitor["homeAway"] == "away":
                        away_abbr = team["abbreviation"]
                        away_score = int(competitor["score"])

            game = Game(week=week, uid=uid, 
                        home_abbr=home_abbr, 
                        away_abbr=away_abbr,
                        home_score=home_score,
                        away_score=away_score,
                        date = gamedate,
                        venue_fullName = venue)
            print(game.debug())

            self.games.append(game)
        # return schedule


    def toJSON(self):
        obj = {
            "meta" : self.meta
        }
        for game in self.games:
            pass
        json_str = json.dumps(obj, indent=4)
        return json_str
