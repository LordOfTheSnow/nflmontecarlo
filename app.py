from Schedule import *
from Conference import *
from Division import *
from Team import *
from League import *

def main():
    nfl = League("NFL")
    afc = Conference("AFC")
    nfl.addConference(afc)
    afcNorth = Division("AFC North")
    afcSouth = Division("AFC South")
    afcEast = Division("AFC East")
    afcWest = Division("AFC West")

    afc.addDivision(afcNorth)
    afc.addDivision(afcSouth)
    afc.addDivision(afcEast)
    afc.addDivision(afcWest)

    chiefs = Team(name="Chiefs", displayName="Kansas City Chiefs", abbreviation="KC", conference=afc, division=afcWest)
    afcWest.addTeam(chiefs)

    nfc = Conference("NFC")
    nfl.addConference(nfc)
    nfcNorth = Division("NFC North")
    nfcSouth = Division("NFC South")
    nfcEast = Division("NFC East")
    nfcWest = Division("NFC West")

    nfc.addDivision(nfcNorth)
    lions = Team(name="Lions", displayName="Detroit Lions", abbreviation="DET", conference=nfc, division=nfcNorth)
    nfcNorth.addTeam(lions)

    nfc.addDivision(nfcWest)
    cardinals = Team(name="Cardinals", displayName="Arizona Cardinals", abbreviation="ARI", conference=nfc, division=nfcWest)
    nfcWest.addTeam(cardinals)

    schedule = Schedule(2023)
    schedule.readData()

    schedule.processGames(afc)
    schedule.processGames(nfc)

    # nfcWest.debug()
    lions.debug()
    cardinals.debug()
    chiefs.debug()

if __name__ == '__main__':
    main()