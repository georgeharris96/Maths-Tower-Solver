from tower import Tower
import numpy as np


class BaseMutator:
    def __init__(self, number_of_mutations: int):
        self.number_of_mutations = number_of_mutations
        pass

    def apply(self, tower_to_mutate: Tower):
        pass
