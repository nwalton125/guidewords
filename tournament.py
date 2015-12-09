from player import Player

#Results are of the form (round, p1_number, p2_number, p1_score, p2_score). The ordering of the names assigns the numbers, so it is significant!
class Tournament:
	#Note: in Tournament, player numbers n go 0≤n≤number of players, so they might have to be adjusted for presenting standings.
	def __init__(self, names):
		self.players = [Player(names[num], num) for num in range(0,len(names))]
		if len(self.players) % 2 == 1:
			self.players.append(Player("Bye", len(names)))
		
		self.num_players = len(self.players)
	
	def enter_game_result(self, result):
		self.players[result[0]].enter_round([result[0],result[2],result[3],result[4]])
		self.players[result[1]].enter_round([result[0],result[1],result[3],result[4]])
		self.players = sorted(self.players, lambda p1, p2: p1.wins-p2.wins if p1.wins != p2.wins else (p2.losses-p1.losses if p1.losses != p2.losses)

	