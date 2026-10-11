
class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.shots = set()

    def place_ship(self, cells):
        ship = set(cells)
        if ship:
            self.ships.append(ship)

    def fire(self, pos):
        self.shots.add(pos)

        for ship in self.ships:
            if pos in ship:
                if ship <= self.shots:
                    return True, ship
                return True, None

        return False, None

    def all_sunk(self):
        return all(ship <= self.shots for ship in self.ships)

    def remaining_cells(self):
        return sum(len(ship - self.shots) for ship in self.ships)
