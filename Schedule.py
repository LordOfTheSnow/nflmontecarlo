from Week import *

class Schedule():
    """represents a whole season schedule"""
 
    def __init__(self, year):
        self.year = year
  
        # create empty list of weeks
        self.weeks = []

    def readData(self):
        # regular season has 18 weeks
        for i in range(1,2):
            week = Week(self.year, i)
            week.readData()
            self.weeks.append(week)
        
        return
    
    def processGames(self, conference):
        for week in self.weeks:
            for game in week.games:
                for division in conference.divisions:
                    for team in division.teams:
                       if game.away_abbr == team.abbreviation:
                            team.points_for += game.away_score
                            team.points_against += game.home_score
                            if game.away_score > game.home_score:
                               team.wins += 1
                            if game.away_score < game.home_score:
                               team.losses += 1
                            if game.away_score == game.home_score:
                               team.ties +=1
                       if game.home_abbr == team.abbreviation:
                            team.points_for += game.home_score
                            team.points_against += game.away_score
                            if game.home_score > game.away_score:
                               team.wins += 1
                            if game.home_score < game.away_score:
                               team.losses += 1
                            if game.home_score == game.away_score:
                               team.ties +=1
        return
 