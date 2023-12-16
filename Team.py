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
        self.wins_in_division = 0
        self.losses_in_division = 0
        self.ties_in_division = 0
        self.wins_in_conference = 0
        self.losses_in_conference = 0
        self.ties_in_conference = 0
        self.points_for = 0
        self.points_against = 0