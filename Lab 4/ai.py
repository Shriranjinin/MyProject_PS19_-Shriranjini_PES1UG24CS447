
import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.hits = set()

    def record_result(self, pos, hit):
        if hit:
            self.hits.add(pos)

    def choose(self):
        adjacent = set()

        for row, col in self.hits:
            adjacent.update({
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            })

        adjacent = {
            pos for pos in adjacent
            if 0 <= pos[0] < self.size
            and 0 <= pos[1] < self.size
            and pos not in self.tried
        }

        if adjacent:
            pos = random.choice(sorted(adjacent))
        else:
            options = [
                (row, col)
                for row in range(self.size)
                for col in range(self.size)
                if (row, col) not in self.tried
            ]

            if not options:
                return None

            pos = random.choice(options)

        self.tried.add(pos)
        return f"{pos[0] + 1},{pos[1] + 1}"
