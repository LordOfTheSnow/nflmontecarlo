class Game(object):
    """represents a single game"""
    def __init__(self, uid, home_abbr, away_abbr, home_score, away_score, date, venue_fullName=""):
        self.uid = uid
        self.home_abbr = home_abbr
        self.away_abbr = away_abbr
        self.home_score = home_score
        self.away_score = away_score
        self.date = date
        self.venue_fullName = venue_fullName

    def debug(self):
        output = f'{self.date}: uid: {self.uid} {self.home_abbr} - {self.away_abbr} @ {self.venue_fullName}: {self.home_score}-{self.away_score}'
        return output