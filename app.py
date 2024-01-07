from Schedule import *
from Conference import *
from Division import *
from Team import *
from League import *

def main():
    teams = {}
    nfl = League("NFL")
    afc = Conference(1,"AFC")
    nfl.addConference(afc)
    afcNorth = Division(1, "AFC North")
    afcEast = Division(2, "AFC East")
    afcSouth = Division(3, "AFC South")
    afcWest = Division(4, "AFC West")

    afc.addDivision(afcNorth)
    afc.addDivision(afcSouth)
    afc.addDivision(afcEast)
    afc.addDivision(afcWest)

    teams["CIN"] = Team(name="Bengals", displayName="Cincinatti Bengals", abbreviation="KC", conference=1, division=1)
    teams["BAL"] = Team(name="Ravens", displayName="Baltimore Ravens", abbreviation="BAL", conference=1, division=1)
    teams["PIT"] = Team(name="Steelers", displayName="Pittsburgh Steelers", abbreviation="PIT", conference=1, division=1)
    teams["CLE"] = Team(name="Browns", displayName="Cleveland Browns", abbreviation="CLE", conference=1, division=1)

    teams["NE"] = Team(name="Patriots", displayName="New England Patriots", abbreviation="NE", conference=1, division=2)
    teams["BUF"] = Team(name="Bills", displayName="Buffalo Bills", abbreviation="BUF", conference=1, division=2)
    teams["MIA"] = Team(name="Dolphins", displayName="Miami Dolphins", abbreviation="MIA", conference=1, division=2)
    teams["NYJ"] = Team(name="Jets", displayName="New York Jets", abbreviation="NYJ", conference=1, division=2)

    teams["HOU"] = Team(name="Texans", displayName="Houston Texans", abbreviation="HOU", conference=1, division=3)
    teams["TEN"] = Team(name="Titans", displayName="Tennessee Titans", abbreviation="TEN", conference=1, division=3)
    teams["JAX"] = Team(name="Jaguars", displayName="Jacksonville Jaguars", abbreviation="JAX", conference=1, division=3)
    teams["IND"] = Team(name="Colts", displayName="Indianapolis Colts", abbreviation="IND", conference=1, division=3)

    teams["KC"] = Team(name="Chiefs", displayName="Kansas City Chiefs", abbreviation="KC", conference=1, division=4)
    teams["LAC"] = Team(name="Chargers", displayName="Los Angeles Chargers", abbreviation="LAC", conference=1, division=4)
    teams["LV"] = Team(name="Raiders", displayName="Las Vegas Raiders", abbreviation="LV", conference=1, division=4)
    teams["DEN"] = Team(name="Broncos", displayName="Denver Broncos", abbreviation="DEN", conference=1, division=4)

    nfc = Conference(2,"NFC")
    nfl.addConference(nfc)
    nfcNorth = Division(5, "NFC North")
    nfcEast = Division(6, "NFC East")
    nfcSouth = Division(7, "NFC South")
    nfcWest = Division(8, "NFC West")

    nfc.addDivision(nfcNorth)
    teams["DET"] = Team(name="Lions", displayName="Detroit Lions", abbreviation="DET", conference=2, division=5)
    teams["GB"] = Team(name="Packers", displayName="Green Bay Packers", abbreviation="GB", conference=2, division=5)
    teams["MIN"] = Team(name="Vikings", displayName="Minnesota Vikings", abbreviation="MIN", conference=2, division=5)
    teams["CHI"] = Team(name="Bears", displayName="Chicago Bears", abbreviation="CHI", conference=2, division=5)

    nfc.addDivision(nfcEast)
    teams["PHI"] = Team(name="Eagles", displayName="Philadelphia Eagles", abbreviation="PHI", conference=2, division=6)
    teams["DAL"] = Team(name="Cowboys", displayName="Dallas Cowboys", abbreviation="DAL", conference=2, division=6)
    teams["WSH"] = Team(name="Commanders", displayName="Washington Commanders", abbreviation="WSH", conference=2, division=6)
    teams["NYG"] = Team(name="Giants", displayName="New York Giants", abbreviation="PHI", conference=2, division=6)

    nfc.addDivision(nfcSouth)
    teams["ATL"] = Team(name="Falcons", displayName="Atlanta Falcons", abbreviation="ATL", conference=2, division=7)
    teams["CAR"] = Team(name="Panthers", displayName="Carolina Panthers", abbreviation="CAR", conference=2, division=7)
    teams["TB"] = Team(name="Buccaneers", displayName="Tampa Bay Buccaneers", abbreviation="TB", conference=2, division=7)
    teams["NO"] = Team(name="Saints", displayName="New Orleans Saints", abbreviation="NO", conference=2, division=7)

    nfc.addDivision(nfcWest)
    teams["ARI"] = Team(name="Cardinals", displayName="Arizona Cardinals", abbreviation="ARI", conference=2, division=8)
    teams["SEA"] = Team(name="Seahawks", displayName="Seattle Seahawks", abbreviation="SEA", conference=2, division=8)
    teams["LAR"] = Team(name="Rams", displayName="Los Angeles Rams", abbreviation="LAR", conference=2, division=8)
    teams["SF"] = Team(name="49ers", displayName="San Francisco 49ers", abbreviation="SF", conference=2, division=8)

    schedule = Schedule(nfl, 2023)
    schedule.readData()

    games = schedule.processGames(teams,completed=True)

    for team in teams:
        teams[team].calculateStats()

    afcNorth.buildDivisionTable(teams)
    afcNorth.rankDivisionTeams(games)
    afcNorth.debug()
    print("")

    afcEast.buildDivisionTable(teams)
    afcEast.rankDivisionTeams(games)
    afcEast.debug()
    print("")

    afcSouth.buildDivisionTable(teams)
    afcSouth.rankDivisionTeams(games)
    afcSouth.debug()
    print("")

    afcWest.buildDivisionTable(teams)
    afcWest.rankDivisionTeams(games)
    afcWest.debug()
    print("")

    nfcNorth.buildDivisionTable(teams)
    nfcNorth.rankDivisionTeams(games)
    nfcNorth.debug()

    print("")

    nfcEast.buildDivisionTable(teams)
    nfcEast.rankDivisionTeams(games)
    nfcEast.debug()

    print("")

    nfcSouth.buildDivisionTable(teams)
    nfcSouth.rankDivisionTeams(games)
    nfcSouth.debug()

    print("")

    nfcWest.buildDivisionTable(teams)
    nfcWest.rankDivisionTeams(games)
    nfcWest.debug()

if __name__ == '__main__':
    main()