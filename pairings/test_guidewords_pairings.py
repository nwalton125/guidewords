import unittest
from pairing import Pairing
from result import Result

#It's an open question whether we want a separate TestCase class for each Guidewords class we are testing. Result and pairing can be tested in the same test case, since Result inherits from pairing and doesn't override anything. But should tournament, player, and result all be in the same test case? Maybe. What about the various pairings functions.

class GuidewordsResultsTestCase(unittest.TestCase):

	def setUp(self):
		global resultA, resultB, resultC
		resultA = Result(3, 3, 375, 4, 275)
		resultB = Result(3, 5, 375, 6, 475)
		resultC = Result(3, 7, 400, 8, 400)

	def tearDown(self):
		pass

	def test_winner_function(self):
		self.assertTrue(resultA.winner() == 3)
		self.assertTrue(resultB.winner() == 6)
		self.assertTrue(resultC.winner() == None)

	def test_is_p1_function(self):
		self.assertTrue(resultA.is_p1(3))
		self.assertFalse(resultA.is_p1(4))
		with self.assertRaises(KeyError):
			resultA.is_p1(5)

	def test_other_player_function(self):
		self.assertTrue(resultA.other_player(3) == 4)
		self.assertTrue(resultA.other_player(4) == 3)
		with self.assertRaises(KeyError):
			resultA.other_player(5)

	#Shouldn't need a 'test_is_p1_function', because Result will end up inheriting from Pairing. If this ends up changing, perhaps we should make a test here.

	def test_spread_function(self):
		self.assertTrue(resultA.spread() == 100)
		self.assertTrue(resultB.spread() == -100)
		self.assertTrue(resultC.spread() == 0)

if __name__ == '__main__':
	unittest.main()


"""def run_player_tests():
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
"""
