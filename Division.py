from operator import itemgetter, attrgetter
from Team import *
import itertools

class Division(object):
    """represents a division"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.teams = []

    def debug(self):
        # print(self.__dict__)
        print(self.name)
        for team in self.teams:
            print(f"{team.name:<16} {team.wins:2d} - {team.losses:2d} - {team.ties:2d}  {team.pct:.3f} | {team.points_for:3d}:{team.points_against:3d} | {team.divisionWins:2d} - {team.divisionLosses:2d} - {team.divisionTies:2d} | {team.divisionPct:.3f} | {team.conferenceWins:2d} - {team.conferenceLosses:2d} - {team.conferenceTies:2d} | {team.conferencePct:.3f} | {team.strength:+2.3f}")

    def buildDivisionTable(self, teams):
        # create a table for the teams in the division
        for team in teams:
            if self.id == teams[team].getDivision():
                self.teams.append(teams[team])
                # teams[team].debug()

    def divisionTiebreaker(self,element):
        return element.pct, element.divisionPct

    def rankDivisionTeams(self, games):
        # first rank teams based upon their winning percentage
        self.teams.sort(key=attrgetter('pct'), reverse=True)

        # slice the division teams based upon their winning percentage
        an_iterator = itertools.groupby(self.teams, lambda x : x.pct)
        for key, group in an_iterator: 
            lgroup = list(group)
            # key_and_group = {key : lgroup} 
            # print(key_and_group, len(lgroup)) 
            if len(lgroup) > 1: # process tiebreaker on teams having the same winning pct
                self.tiebreakGroup(lgroup, games)

    #   self.teams.sort(key=self.divisionTiebreaker, reverse=True)

    def tiebreakGroup(self, teams, games):
        team1Pct = 0.0
        team2Pct = 0.0
        for i in range(0, len(teams)):
            team1 = teams[i]
            for j in range(i+1, len(teams)):
                team2 = teams[j]
                team1Pct, team2Pct = self.headToHead(games, team1.abbreviation, team2.abbreviation)
                print(f"{team1.name}-{team2.name}: {team1Pct}-{team2Pct}")

    def headToHead(self, games, team1Abbr, team2Abbr):
        gamekey1 = team1Abbr + team2Abbr
        gamekey2 = team2Abbr + team1Abbr

        game1 = self.findGame(games, gamekey1)
        game2 = self.findGame(games, gamekey2)
        
        team1Pct = 0.0
        team2Pct = 0.0

        if game1:
            if game1.home_score > game1.away_score:
                team1Pct = 1.0
            elif game1.home_score < game1.away_score:
                team2Pct = 1.0
            else:
                team1Pct = team2Pct = 0.5
            # print(game1.home_abbr, game1.home_score)
            # print(game1.away_abbr, game1.away_score)
        if game2:
            if game2.home_score > game2.away_score:
                team2Pct += 1.0
            elif game2.home_score < game2.away_score:
                team1Pct += 1.0
            else:
                team1Pct += 0.5
                team2Pct += 0.5
            # print(game2.home_abbr, game2.home_score)
            # print(game2.away_abbr, game2.away_score)

        return team1Pct, team2Pct
    
    def findGame(self, games, gamekey):
        for game in games:
            if game.key == gamekey:
                return game
        return None
