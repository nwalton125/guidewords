class Pairing:
    def __init__(self, round, p1Seed, p2Seed):
        self.round  = round
        self.p1Seed = p1Seed
        self.p2Seed = p2Seed

    #This function is used by functions in the player class.
    def is_p1(self, seed):
        if seed in [self.p1Seed, self.p2Seed]:
            return seed == self.p1Seed
        else:
            raise KeyError('The given seed was not contained in this pairing object.')

    #This function is used by functions in the player class.
    def other_player(self, seed):
        if self.is_p1(seed):
            return self.p2Seed
        else:
            return self.p1Seed
