class Team(object):
    """represents a team"""
    def __init__(self, name, displayName, abbreviation, conference, division):
        self.name = name
        self.displayName = displayName
        self.abbreviation = abbreviation
        self.conference = conference
        self.division = division
        
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.divisionWins = 0
        self.divisionLosses = 0
        self.divisionTies = 0
        self.conferenceWins = 0
        self.conferenceLosses = 0
        self.conferenceTies = 0
        self.points_for = 0
        self.points_against = 0

        self.pct = 0.0
        self.strength = 1.0

    def debug(self):
        print(self.__dict__)

    def calculateStats(self):
        if (self.wins + self.losses + self.ties) > 0:
            self.pct = (self.wins + self.ties * 0.5) / (self.wins + self.losses + self.ties)