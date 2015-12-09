from tournament import Tournament
from player import Player

#Pairings functions return a list of ordered pairs p, so that for each p, p[0] plays p[1]. (This is tentative, and may not work as well for Portland-style pairings as it does for KOTH! Or maybe it's a bad data format altogether!)

#KOTH is an abbreviation for "king-of-the-hill".
def koth(tourney):
	return [(tourney.players[2*pair_number].seed, tourney.players[2*pair_number+1].seed) for pair_number in range(0,tourney.num_players/2)]
	#Does a longer version of this return statement make it easier to read?

def round_robin(tourney, num_games):
	if num_games % 2 == 0:
		