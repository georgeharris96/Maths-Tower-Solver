import numpy as np
import random


class Tower:
    def __init__(self):
        self.blocks = np.empty((0, 4), int)

    def __len__(self):
        return len(self.blocks)

    def add_block(self, blocks_to_add: list):
        self.blocks = np.concatenate((self.blocks, blocks_to_add), axis=0)

    def add_blocks_from_file(self, file_dir: str):
        with open(file_dir, "r") as f:
            for block in f.readlines():
                self.add_block(
                    block.split(",")
                )

    def reset(self):
        self.blocks = np.array([])

    def rotate_right(self, position: int):
        idx = [3, 0, 1, 2]
        block = self.blocks[position]
        self.blocks[position] = block[idx]

    def rotate_left(self, position: int):
        idx = [1, 2, 3, 0]
        block = self.blocks[position]
        self.blocks[position] = block[idx]

    def randomise(self):
        direction_idx = {
            0: [3, 0, 1, 2],
            1: [1, 2, 3, 0]
        }
        for i, block in enumerate(self.blocks):
            direction = random.randint(0, 1)
            rotations = random.randint(0, 100)

            for j in range(rotations):
                self.blocks[i] = block[direction_idx[direction]]

    def calculate_totals_errors(self):
        totals = np.sum(self.blocks, axis=0)
        return totals, np.mean(abs(555 - totals))
