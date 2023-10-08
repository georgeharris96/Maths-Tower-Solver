import numpy as np

class BaseCrossover:
    def __init__(self):
        pass

    def apply(self, towers_to_combine: list):
       pass


class OnePointCrossover(BaseCrossover):
    def __int__(self):
        pass

    def apply(self, towers_to_combine: list):
        tower_0 = towers_to_combine[0]
        tower_1 = towers_to_combine[1]

        cut_point = np.random.randint(low=0, high=10)

        if cut_point > len(tower_0)/2:
            child_start = tower_0.blocks[:cut_point]
            child_end = tower_1.blocks[cut_point:]
            child = np.concatenate((child_start, child_end))
        return child
    