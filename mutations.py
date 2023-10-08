from tower import Tower
import numpy as np


class BaseMutator:
    def __init__(self, number_of_mutations: int):
        self.number_of_mutations = number_of_mutations
        pass

    def apply(self, tower_to_mutate: Tower):
        pass


class SingularSwapper(BaseMutator):
    def apply(self, tower_to_mutate: Tower):
        new_towers = []
        blocks_to_rotate = np.random.randint(low=0, high=10, size=self.number_of_mutations)
        direction = np.random.randint(low=0, high=2, size=self.number_of_mutations)

        for i in range(self.number_of_mutations):

            if direction[i] == 1:
                new_towers.append(tower_to_mutate.rotate_left(blocks_to_rotate[i]))
            else:
                new_towers.append(tower_to_mutate.rotate_right(blocks_to_rotate[i]))
        return new_towers
