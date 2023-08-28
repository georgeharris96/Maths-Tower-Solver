import numpy as np

from tower import Tower
import copy


# todo add mutation and combination method types
class TowerSolver:
    def __init__(self, base_tower: Tower, mutation_method, combination_method,):
        self.base_tower = base_tower
        self.tower_history = [base_tower]
        self.mutation_method = mutation_method
        self.combination_method = combination_method
        self.error_history = []
        self.last_error = None
        self.generations = 0
        pass

    def _mutate_tower(self, tower_to_mutate: Tower):
        return self.mutation_method(tower_to_mutate)

    def _combine_towers(self, towers_to_combine: list):
        return self.combination_method(towers_to_combine)

    def _copy_tower(self, number_of_mutations):
        return [copy.deepcopy(self.base_tower) for _ in range(number_of_mutations)]

    def solve(self, number_of_generations: int, number_of_mutations: int):
        while self.last_error != 0 or number_of_generations != self.generations:
            # Create copies of tower
            new_towers = self._copy_tower(number_of_mutations)

            # Mutate copies of base tower
            for i, tower in enumerate(new_towers):
                # Mutate copies of base tower
                new_towers[i] = self._mutate_tower(tower_to_mutate=tower)

            # Calculate error across all towers
            errors_across_all_towers = [tower.calculate_totals_errors()[1] for tower in new_towers]

            if 0 not in errors_across_all_towers:
                # Combine two best to create new base tower
                self.base_tower = self._combine_towers(
                    towers_to_combine=[
                        np.argpartition(errors_across_all_towers, kth=2)[0],
                        np.argpartition(errors_across_all_towers, kth=2)[1]
                    ]
                )
                self.error_history.append(np.argpartition(errors_across_all_towers, kth=2)[0])
                self.last_error = self.base_tower.calculate_totals_errors()[1]

                self.generations += 1
            else:
                # Return solved tower
                self.error_history.append(0)
                return new_towers[np.argpartition(errors_across_all_towers, kth=2)[0]]

        return self.base_tower, self.generations
