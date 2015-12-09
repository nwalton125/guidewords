#Results are of the form (round, opponent_number, player_score, opponent_score).
class Player:
	def __init__(self, name, seed = 0, results = []):
		self.name    = name
		self.seed    = seed
	
		self.results = sorted(results)
		
		self.wins    = len(filter(lambda result: result[0] > result[1], self.results))
		self.losses  = len(filter(lambda result: result[0] < result[1], self.results))
		self.draws   = len(self.results)-self.wins-self.losses
		
		self.spread  = sum([result[2] for result in self.results]) - sum([result[3] for result in self.results])
	
	def enter_round(self, new_round):
		self.results = sorted(self.results+[new_round])
		
		if new_round[2] > new_round[3]:
			self.wins   += 1
		elif new_round[2] < new_round[3]:
			self.losses += 1
		else:
			self.draws  += 1
		
		self.spread += (new_round[2]-new_round[3])
		
