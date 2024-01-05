from operator import itemgetter, attrgetter
from Team import *

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

    def rankDivisionTeams(self):
      self.teams.sort(key=self.divisionTiebreaker, reverse=True)
