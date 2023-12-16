class Conference(object):
    """represents a conference"""
    def __init__(self,name):
        self.name=name
        self.divisions = []

    def addDivision(self, division):
        self.divisions.append(division)
