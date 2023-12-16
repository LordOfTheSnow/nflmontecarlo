from Week import *

class Schedule():
    """represents a whole season schedule"""
 
    def __init__(self, year):
        self.year = year
  
        # create empty list of weeks
        self.weeks = []

        # regular season has 18 weeks
        for i in range(1,19):
            week = Week(self.year, i)
            key = "week" + str(i)
            value = week.readData()
            self.weeks.append({key : value})
 