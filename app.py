from Schedule import *
from Conference import *
from Division import *
from Team import *
from League import *

def main():
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

    chiefs = Team(name="Chiefs", displayName="Kansas City Chiefs", abbreviation="KC", conference=1, division=4)
    afcWest.addTeam(chiefs)

    nfc = Conference(2,"NFC")
    nfl.addConference(nfc)
    nfcNorth = Division(5, "NFC North")
    nfcEast = Division(6, "NFC East")
    nfcSouth = Division(7, "NFC South")
    nfcWest = Division(8, "NFC West")

    nfc.addDivision(nfcNorth)
    lions = Team(name="Lions", displayName="Detroit Lions", abbreviation="DET", conference=2, division=5)
    nfcNorth.addTeam(lions)

    nfc.addDivision(nfcWest)
    cardinals = Team(name="Cardinals", displayName="Arizona Cardinals", abbreviation="ARI", conference=2, division=8)
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