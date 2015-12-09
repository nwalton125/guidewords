from player import Player

def run_player_tests():
	all_tests_passed = True

	amalan = Player("Amalan")
	noah = Player("Noah", 1, [2, 4, 630, 730])
	amalan.enter_round([3, 3, 400, 450])
	amalan.enter_round([1, 5, 340,230])
	noah.enter_round([1, 6, 440, 440])
	noah.enter_round([3, 3, 530, 8])
	amalan.enter_round([2, 2, 430, 430])


	if amalan.name() != "Amalan":
		all_tests_passed = False
	if noah.name() != "Noah":
	
	if amalan.seed() != 0:

	if noah.seed() != 0:

	if amalan.results() != [[1,5,340,230],[2,2,430,430],[3,3,400,450]]:

	if noah.results() != [[1,6,440,440],[2,4,630,730],