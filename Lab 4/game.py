from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        self.player.place_ship({(1, 1), (1, 2), (1, 3)})
        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)})

    def show(self):
        print("\nYour shots are coordinates like 2,3.")
        remaining = len(self.enemy.ships - self.enemy.shots)
        print("Enemy ship cells remaining:", remaining)

    def run(self):
        print("Battleship")

        while True:
            self.show()
            raw = input("> ").strip().lower()

            if raw == "q":
                print("Game ended.")
                return

            try:
                parts = raw.split(",")
                if len(parts) != 2:
                    raise ValueError

                r, c = map(int, parts)
                pos = (r - 1, c - 1)

            except ValueError:
                print("Invalid input. Enter coordinates like 2,3.")
                continue

            if not (0 <= pos[0] < Board.SIZE and
                    0 <= pos[1] < Board.SIZE):
                print("Outside board. Choose coordinates from 1 to 6.")
                continue

            if pos in self.enemy.shots:
                print("Already fired there. Choose another cell.")
                continue

            if self.enemy.fire(pos):
                print("HIT!")
            else:
                print("MISS!")

            if self.enemy.all_sunk():
                print("You sank the enemy fleet. You win!")
                return

            ai_pos = self.ai.choose()

            try:
                ar, ac = map(int, ai_pos.split(","))
                player_pos = (ar - 1, ac - 1)

                if not (0 <= player_pos[0] < Board.SIZE and
                        0 <= player_pos[1] < Board.SIZE):
                    print("AI generated an invalid move.")
                    continue

            except (ValueError, AttributeError):
                print("AI generated an invalid move.")
                continue

            print("AI fired at", ai_pos)

            if self.player.fire(player_pos):
                print("AI scored a hit!")
            else:
                print("AI missed.")

            if self.player.all_sunk():
                print("The AI sank your fleet. Game over!")
                return