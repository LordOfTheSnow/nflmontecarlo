class Conference(object):
    """represents a conference"""
    def __init__(self, id, name):
        self.id=id
        self.name=name
        self.divisions = []

    def addDivision(self, division):
        self.divisions.append(division)
