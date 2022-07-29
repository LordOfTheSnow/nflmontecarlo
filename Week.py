import re
import urllib.request, json
from Game import *

class Week():
    """represents a week with Games"""
    baseURL = "https://www.espn.com/nfl/schedule/_/year/2021/week/1?xhr=1"

    def __init__(self, year, week):
        self.year = year
        self.week = week

        # replace year/week in base URL to be used with specific values
        self.url = re.sub("year/(\d{4})", f"year/{str(self.year)}", self.baseURL)
        self.url = re.sub("week/(\d+)", f"week/{str(self.week)}", self.url)
        # print(self.url)

        # create empty list of games; games will be appended in readData() function
        self.games = []

    def readData(self):
        with urllib.request.urlopen(self.url) as url:
            data = json.loads(url.read().decode())
            self.meta = data["meta"]
            self.content = data["content"]
            schedule = self.content["schedule"]

            for gameday_key, gameday_value in schedule.items():
                # print(gameday_key)
                games = gameday_value
                for game_key,game_value in games.items():
                    for single_game in game_value:
                        competions = single_game["competitions"]
                        venue = competions[0]["venue"]
                        competitors = competions[0]["competitors"]
                        if competitors[0]["homeAway"] == "home":
                            home = competitors[0]
                        if competitors[0]["homeAway"] == "away":
                            away = competitors[0]
                        if competitors[1]["homeAway"] == "home":
                            home = competitors[1]
                        if competitors[1]["homeAway"] == "away":
                            away = competitors[1]
                        home_score = home["score"]
                        away_score = away["score"]
                        home_team = home["team"]
                        away_team = away["team"]

                        game = Game(uid=single_game["uid"], 
                                    home_abbr=home_team["abbreviation"],
                                    away_abbr=away_team["abbreviation"],
                                    home_score=home_score,
                                    away_score=away_score,
                                    date=single_game["date"],
                                    venue_fullName=venue["fullName"])
                        print(game.debug())

                        self.games.append(game)
            return schedule

    def toJSON(self):
        obj = {
            "meta" : self.meta
        }
        for game in self.games:
            pass
        json_str = json.dumps(obj, indent=4)
        return json_str
