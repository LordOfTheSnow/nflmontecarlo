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

    teams["KC"] = Team(name="Chiefs", displayName="Kansas City Chiefs", abbreviation="KC", conference=1, division=4)

    nfc = Conference(2,"NFC")
    nfl.addConference(nfc)
    nfcNorth = Division(5, "NFC North")
    nfcEast = Division(6, "NFC East")
    nfcSouth = Division(7, "NFC South")
    nfcWest = Division(8, "NFC West")

    nfc.addDivision(nfcNorth)
    teams["DET"] = Team(name="Lions", displayName="Detroit Lions", abbreviation="DET", conference=2, division=5)

    nfc.addDivision(nfcWest)
    teams["ARI"] = Team(name="Cardinals", displayName="Arizona Cardinals", abbreviation="ARI", conference=2, division=8)
    teams["ATL"] = Team(name="Falcons", displayName="Atlanta Falcons", abbreviation="ATL", conference=2, division=7)
    teams["CAR"] = Team(name="Panthers", displayName="Carolina Panthers", abbreviation="CAR", conference=2, division=7)
    teams["SEA"] = Team(name="Seahawks", displayName="Seattle Seahawks", abbreviation="SEA", conference=2, division=8)
    teams["LAR"] = Team(name="Rams", displayName="Los Angeles Rams", abbreviation="LAR", conference=2, division=8)
    teams["SF"] = Team(name="49ers", displayName="San Francisco 49ers", abbreviation="SF", conference=2, division=8)

    schedule = Schedule(2023)
    schedule.readData()

    schedule.processGames(teams)

    for team in teams:
        teams[team].calculateStats()

    # nfcWest.debug()
    teams["DET"].debug()
    teams["ARI"].debug()
    teams["KC"].debug()
    teams["ATL"].debug()
    teams["CAR"].debug()
    teams["SEA"].debug()
    teams["LAR"].debug()
    teams["SF"].debug()

if __name__ == '__main__':
    main()