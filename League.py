class League(object):
    """represents a League"""
    def __init__(self, name):
        self.name=name
        self.conferences = []

    def addConference(self, conference):
        self.conferences.append(conference)

    def getName(self):
        return self.name