class Division(object):
    """represents a division"""
    def __init__(self,name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)
