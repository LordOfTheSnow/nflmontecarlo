import math
from Week import *

class Schedule():
    """represents a whole season schedule"""
 
    def __init__(self, league, year):
        self.league = league
        self.year = year
  
        # create empty lists of weeks and games
        self.weeks = []
        self.games = []

    def readData(self):
        # regular season has 18 weeks
        for i in range(1,19):
            week = Week(self.league.getName(), self.year, i)
            week.readData()
            week.writeData(self.league.getName(), self.year, i)
            self.weeks.append(week)
        
        return
    
    def processGames(self, teams, completed=True):
        for week in self.weeks:
            for game in week.games:
                if completed == False or (completed == True and game.completed == True):
                    if game.home_abbr in teams and game.away_abbr in teams:
                        hometeam = teams[game.home_abbr]
                        awayteam = teams[game.away_abbr]

                        hometeam.points_for += game.home_score
                        hometeam.points_against += game.away_score
                        awayteam.points_for += game.away_score
                        awayteam.points_against += game.home_score

                        # avoid divison by zero or invalid log values
                        homescoreval = 1 if game.home_score == 0 else game.home_score
                        awayscoreval = 1 if game.away_score == 0 else game.away_score
                        homestrengthfactor = math.log10(homescoreval / awayscoreval)
                        awaystrengthfactor = math.log10(awayscoreval / homescoreval)
                        hometeam.strength += homestrengthfactor
                        awayteam.strength += awaystrengthfactor

                        if game.away_score > game.home_score:
                            awayteam.wins += 1
                            hometeam.losses += 1
                            if hometeam.division == awayteam.division:
                                awayteam.divisionWins +=1
                                hometeam.divisionLosses += 1
                            if hometeam.conference == awayteam.conference:
                                awayteam.conferenceWins += 1
                                hometeam.conferenceLosses += 1    
                        elif game.away_score < game.home_score:
                            awayteam.losses += 1
                            hometeam.wins += 1
                            if hometeam.division == awayteam.division:
                                awayteam.divisionLosses +=1
                                hometeam.divisionWins += 1
                            if hometeam.conference == awayteam.conference:
                                awayteam.conferenceLosses += 1
                                hometeam.conferenceWins += 1    
                        elif  game.away_score == game.home_score:
                            awayteam.ties += 1
                            hometeam.ties += 1
                            if hometeam.division == awayteam.division:
                                awayteam.divisionTies +=1
                                hometeam.divisionTies += 1
                            if hometeam.conference == awayteam.conference:
                                awayteam.conferenceTies += 1
                                hometeam.conferenceTies += 1
                        
                        self.games.append(game)

        return self.games
 

