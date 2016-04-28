from result import Result

#Results are of the form (round, opponent_number, player_score, opponent_score). A player's results are organized by round. Pairings are of the form (round, opponent_number). Possible additions to this would be the player's rating and provisional status, but for simplicity we won't include those (yet).
class Player:
	def __init__(self, name, seed, results = [], pairings = []):
		self.name    = name
		self.seed    = seed
		self.results   = sorted(results,  key = self.round)
		self.pairings  = sorted(pairings, key = self.round)

	#Note that some seeds may be included more than once in opp_seeds.
	def opp_seeds(self):
		return [pairing.other_player(self.seed) for pairing in self.pairings()]

	def num_wins(self):
		return len(filter(lambda result: result.winner() == seed, self.results)

	def num_losses(self):
		return len(filter(lambda result: result.winner() not in [seed, None], self.results)

	def num_draws(self):
		return len(filter(lambda result: result.winner() == None), self.results)

	def spread(self):
		total = 0
		for result in self.results:


	def enter_round(self, new_result):
		self.results = sorted(self.results+[new_result], key = self.round)

	#Note: it's possible we'd also want a function like #"number_of_games_against_opponent", if we anticipate that late-tourney pairings
	#will use this datum.
	def has_played_opponent(self, opp_seed):
		if opp_seed in self.opp_seeds():
			return True
		else:
			return False
