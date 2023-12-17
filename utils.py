from Team import *

def getTeamByAbbreviation(teams, abbreviation):
    for team in teams:
        if team["abbreviation"] == abbreviation:
            return team
    
    # team not found, return None
    return None