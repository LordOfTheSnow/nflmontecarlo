class Game(object):
    """represents a single game"""
    def __init__(self, week, uid, home_abbr, away_abbr, home_score, away_score, date, completed, venue_fullName=""):
        self.week = week
        self.uid = uid
        self.home_abbr = home_abbr
        self.away_abbr = away_abbr
        self.home_score = home_score
        self.away_score = away_score
        self.date = date
        self.completed = completed
        self.venue_fullName = venue_fullName
        self.key = home_abbr + away_abbr # set this as a key to easily find a game between to teams

    def debug(self):
        output = f'Week {self.week} - {self.date}: {self.home_abbr} - {self.away_abbr} @ {self.venue_fullName}: {self.home_score}-{self.away_score} | {self.completed}'
        return output