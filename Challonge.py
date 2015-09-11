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
        self.ids = [playerID]
        self.place = placing
        if placing == 32:
            self.points = 400
        elif placing == 33:
            self.points = 0
        else:
            self.points = 500

#---------------------------------------------------------- Tournament Class
        
class Tournament:
    def __init__(self, participantData, matchData, tID, isPool):
        self.playerData = participantData
        self.matchData = matchData
        self.ID = tID
        self.isPool = isPool

#----------------------------------------------------------
# Pull down and store data for all tournaments used
# Flashback 14
tournaments = [Tournament(participantsData, matchData, 123, False)]

tournament = challonge.tournaments.show("FBGT14p1")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p2")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p3")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p4")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p5")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p6")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT14p7")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

#----------------------------------------------------------------------
# Flashback 15
tournament = challonge.tournaments.show("FBGT15")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, False))

tournament = challonge.tournaments.show("FBGT15p1")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p2")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p3")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p4")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p5")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p6")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p7")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p8")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p9")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT15p10")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))
#----------------------------------------------------------------------
# Flashback 16

tournament = challonge.tournaments.show("FBGT16")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, False))

tournament = challonge.tournaments.show("FBGT16p1")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p2")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p3")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p4")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p5")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p6")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p7")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p8")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p9")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))

tournament = challonge.tournaments.show("FBGT16p10")
participantsData = challonge.participants.index(tournament["id"])
matchData = challonge.matches.index(tournament["id"])
tournaments.append(Tournament(participantsData, matchData, 123, True))
#----------------------------------------------------------------------
# Form a database of all players across tournaments used
playersByTag = {}

tournaments.sort(key=lambda x: x.isPool)

for t in tournaments:
    print t.isPool
    for pl in t.playerData:
        if pl['display-name'][:3] == 'BYE':
            if pl['display-name'] in playersByTag:
                playersByTag[pl['display-name']].ids.append(pl['id'])
            else:
                playersByTag[pl['display-name']] = (Player(pl['display-name'], pl['id'], 33))           
        elif t.isPool:
            if pl['display-name'] in playersByTag:
                playersByTag[pl['display-name']].ids.append(pl['id'])
            else:
                playersByTag[pl['display-name']] = (Player(pl['display-name'], pl['id'], 32))                
        else:
            if pl['display-name'][:-2] in playersByTag:
                playersByTag[pl['display-name'][:-2]].ids.append(pl['id'])
            else:
                if pl['final-rank'] is None:
                    playersByTag[pl['display-name'][:-2]] = (Player(pl['display-name'][:-2], pl['id'], -1))                
                else:
                    playersByTag[pl['display-name'][:-2]] = (Player(pl['display-name'][:-2], pl['id'], pl['final-rank']))                
                         
# Generate player pool - dict indexed by challonge id
playerPool = {}

for tag in playersByTag:
    for pID in playersByTag[tag].ids:
        playerPool[pID] = playersByTag[tag]

# Loop through tournament matches, transferring points from loser to winner
# based on match results
for tnmt in tournaments:
    for tm in tnmt.matchData:
        if tm['player1-id'] is not None:
            P1 = playerPool[tm['player1-id']]
            P2 = playerPool[tm['player2-id']]

        if tm['scores-csv'] is not None and tm['scores-csv'][0] is not '-':
            P1wins = int(tm['scores-csv'][0])
            P2wins = int(tm['scores-csv'][-1])

            if P1wins >= 0 and P2wins >= 0 and len(tm['scores-csv']) <= 3:
                P1PointsGained = .05 * P1wins * P2.points
                P2PointsGained = .05 * P2wins * P1.points

                P1.points += P1PointsGained - P2PointsGained
                P2.points += P2PointsGained - P1PointsGained
                
# Spit out players in sorted order

Results = []

for tag in playersByTag:
    Results.append([tag, playersByTag[tag].points])


SortedResults = sorted(Results, key=itemgetter(1), reverse=True)


for idx, result in enumerate(SortedResults):
    print idx+1, result[0], result[1]
    
