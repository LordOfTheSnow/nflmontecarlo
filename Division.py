class Division(object):
    """represents a division"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def debug(self):
        print(self.__dict__)
