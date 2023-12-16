from Schedule import *
from Conference import *
from Division import *
from Team import *

def main():
    afc = Conference("AFC")
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
    nfcNorth = Division("NFC North")
    nfc.addDivision(nfcNorth)
    lions = Team(name="Lions", displayName="Detroit Lions", abbreviation="DET", conference=nfc, division=nfcNorth)
    nfcNorth.addTeam(lions)

    schedule = Schedule(2023)
    schedule.readData()

    schedule.processGames(afc)
    schedule.processGames(nfc)
    print("done.")

if __name__ == '__main__':
    main()