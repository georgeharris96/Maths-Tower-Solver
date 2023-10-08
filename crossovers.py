import numpy as np

class BaseCrossover:
    def __init__(self):
        pass

    def apply(self, towers_to_combine: list):
       pass


class OnePointCrossover(BaseCrossover):
    def apply(self, towers_to_combine: list):
        tower_0 = towers_to_combine[0]
        tower_1 = towers_to_combine[1]

        cut_point = np.random.randint(low=0, high=10)

        if cut_point > len(tower_0)/2:
            child_start = tower_0.blocks[:cut_point]
            child_end = tower_1.blocks[cut_point:]
            child = np.concatenate((child_start, child_end))
        return child


class WeightedUniformCrossover(BaseCrossover):
    def apply(self, towers_to_combine: list):
        child = np.array([])
        tower_0 = towers_to_combine[0]
        tower_1 = towers_to_combine[1]
        mixing_ratio = tower_0.calculate_totals_errors()[0]/tower_1.calculate_total_errors()[1]
        for block_0, block_1 in zip(tower_0.block, tower_1.blocks):
            random_int = np.random.binomial(n=1, p=mixing_ratio)

            if random_int == 1:
                child.append(block_0)
            else:
                child.append(block_1)

        return child
