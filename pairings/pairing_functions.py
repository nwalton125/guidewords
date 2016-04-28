from tournament import Tournament
from player import Player
from copy import deepcopy

#Pairings functions return a list of ordered pairs p, so that for each p, p[0] plays p[1]. (This is tentative, and may not work as well for Portland-style pairings as it does for KOTH! Or maybe it's a bad data format altogether!)

#How can we do pairings Portland-style? One idea is to give each player a set of opponents, which 
#allows us to record opponents without recording results, so players can be seen as having been
#paired with opponent, without actually having a game results entry for them. 

#KOTH is an abbreviation for "king-of-the-hill". Currently, this form of the function does
#not use the Gibson rule.
def koth(tourney):
	return [(tourney.players[2*pair_number].seed, tourney.players[2*pair_number+1].seed) for pair_number in range(0,tourney.num_players/2)]
	#Does a longer version of this return statement make it easier to read?



"""def round_robin(tourney, num_games):
	if num_games % 2 == 0:
"""

def swiss_pairings(tourney):
	pairings = []
	
	#Is it bad object-oriented design to access objects in this way?
	unpaired_seeds = [tourney.players.seed for player in tourney.players]
	while unpaired_seeds != []:
		curr_seed = unpaired_seeds[0]
		for seed in unpaired_seeds[1:]:
			if 
		