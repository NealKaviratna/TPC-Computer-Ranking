import challonge
from operator import itemgetter, attrgetter, methodcaller

# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
challonge.set_credentials("Timepilotchkn", "dYDXkiKtJQMBekM6RQntuesUGWwc3nTlslME5FLv")

# Retrieve a tournament by its id (or its url).
tournament = challonge.tournaments.show("FBGT14")

# Tournaments, matches, and participants are all represented as normal Python dicts.
print(tournament["id"]) # 3272
print(tournament["name"]) # My Awesome Tournament
print(tournament["started-at"]) # None

# Retrieve the participants for a given tournament.
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
#print(matchData[0])


#---------------------------------------------------------- Player Class

class Player:
    def __init__(self, tagData, playerID, placing):
        self.tag = tagData
        self.ID = playerID
        self.place = placing
        self.points = 1000.0 - ((placing - 1) * 31.25)

#---------------------------------------------------------- Tournament Class
        
class Tournament:
    def __init__(self, participantData, matchData, tID, isPool):
        self.playerData = participantData
        self.matchData = matchData
        self.ID = tID
        self.isPool = isPool

#----------------------------------------------------------
tournaments = []

playerByTag = {}

for t in tournaments:
    for pl in participantsData:
        if not t.isPool:
            playerByTag[pl['display-name']] = (Player(pl['display-name'][:-2], pl['id'], pl['final-rank']))
        else:
            playerByTag[pl['display-name']] = (Player(pl['display-name'][:-2], pl['id'], 33))
            
# Generate player pool - dict indexed by challonge id
playerPool = {}

# Loop through tournament matches, transferring points from loser to winner
# based on match results
for tm in matchData:
    P1 = playerPool[tm['player1-id']]
    P2 = playerPool[tm['player2-id']]
    P1wins = int(tm['scores-csv'][0])
    P2wins = int(tm['scores-csv'][-1])

    P1PointsGained = .05 * P1wins * P2.points
    P2PointsGained = .05 * P2wins * P1.points

    P1.points += P1PointsGained - P2PointsGained
    P2.points += P2PointsGained - P1PointsGained

# Spit out players in sorted order

Results = []

for ID in playerPool:
    Results.append([playerPool[ID].tag, playerPool[ID].points])


SortedResults = sorted(Results, key=itemgetter(1), reverse=True)

for result in SortedResults:
    print result[0], result[1]
    
