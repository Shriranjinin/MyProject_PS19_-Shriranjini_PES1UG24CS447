
from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI(Board.SIZE)
        self._setup()

    def _setup(self):
        self.player.place_ship({(1, 1), (1, 2), (1, 3)})
        self.player.place_ship({(4, 4), (4, 5)})

        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)})
        self.enemy.place_ship({(4, 0), (5, 0)})

    def show(self):
        print("\nYour shots are coordinates like 2,3 (or q to quit).")
        print("Enemy ship cells remaining:", self.enemy.remaining_cells())

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

                row, col = map(int, parts)
                pos = (row - 1, col - 1)

            except ValueError:
                print("Invalid input. Enter coordinates like 2,3.")
                continue

            if not (
                0 <= pos[0] < Board.SIZE
                and 0 <= pos[1] < Board.SIZE
            ):
                print("Outside board. Choose coordinates from 1 to 6.")
                continue

            if pos in self.enemy.shots:
                print("Already fired there. Choose another cell.")
                continue

            hit, sunk_ship = self.enemy.fire(pos)

            if hit:
                print("HIT!")
                if sunk_ship is not None:
                    print("You sank an enemy ship!")
            else:
                print("MISS!")

            if self.enemy.all_sunk():
                print("You sank the enemy fleet. You win!")
                return

            ai_move = self.ai.choose()

            if ai_move is None:
                print("AI has no untried cells remaining.")
                return

            try:
                ai_row, ai_col = map(int, ai_move.split(","))
                player_pos = (ai_row - 1, ai_col - 1)
            except (ValueError, AttributeError):
                print("AI generated an invalid move.")
                return

            if not (
                0 <= player_pos[0] < Board.SIZE
                and 0 <= player_pos[1] < Board.SIZE
            ):
                print("AI generated an invalid move.")
                return

            print("AI fired at", ai_move)

            ai_hit, ai_sunk_ship = self.player.fire(player_pos)
            self.ai.record_result(player_pos, ai_hit)

            if ai_hit:
                print("AI scored a hit!")
                if ai_sunk_ship is not None:
                    print("AI sank one of your ships!")
            else:
                print("AI missed.")

            if self.player.all_sunk():
                print("The AI sank your fleet. Game over!")
                return
