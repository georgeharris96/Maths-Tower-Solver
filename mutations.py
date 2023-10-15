from tower import Tower
import numpy as np


class BaseMutator:
    def __init__(self, number_of_mutations: int):
        self.number_of_mutations = number_of_mutations
        pass

    def apply(self, tower_to_mutate: Tower):
        pass


class BitStringStyleMutator(BaseMutator):
    def apply(self, tower_to_mutate: Tower):
        probability_to_mutate = 1/len(tower_to_mutate)
        for block_i in range(len(tower_to_mutate)):
            if np.random.binomial(n=1, p=probability_to_mutate) == 1:
                if np.random.binomial(n=1, p=probability_to_mutate) == 1:
                    tower_to_mutate.rotate_right(position=block_i)
                else:
                    tower_to_mutate.rotate_left(position=block_i)
        return tower_to_mutate
    