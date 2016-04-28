from pairing import Pairing

#Since results are basically more specific versions of pairings, it would be a good idea to rewrite so that Result inherits from Pairing. But before doing this, let's write some tests!

class Result(Pairing):
    #Currently, it doesn't seem that player names are needed in results, but that could change. It should be easy to fix, because seeds, and not names, are what are used to make pairings.
    def __init__(self, round, p1Seed, p1Score, p2Seed, p2Score):
        Pairing.__init__(self, round, p1Seed, p2Seed)
        self.p1Score = p1Score
        self.p2Score = p2Score

    def winner(self):
        if self.p1Score > self.p2Score:
            return self.p1Seed
        elif self.p1Score < self.p2Score:
            return self.p2Seed
        else:
            return None #None is returned because in a draw, there is no winner.

    #This function is used by functions in the player class.
#    def is_p1(self, seed):
#        if seed in [self.p1Seed, self.p2Seed]:
#            return seed == self.p1Seed
#        else:
#            raise KeyError('The given seed was not contained in this pairing object.')

    #Note that the spread is recorded from the perspective of player1.
    def spread(self):
        return self.p1Score - self.p2Score
