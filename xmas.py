import re

class Grid:

    def __init__(self):
        self.lit = set()

    @property
    def lit_count(self):
        return len(self.lit)

    def act(self, command):
        corner1, corner2 = re.search(r'.+(\d,\d) through (\d,\d)', command).groups()

        positions = [
            f'0,{i}' for i in range(int(corner1[-1]), int(corner2[-1]) + 1)
        ]
        print(positions)
        for pos in positions:
            if 'toggle' in command:
                if pos in self.lit:
                    self.lit.remove(pos)
                else:
                    self.lit.add(pos)

            if 'turn on' in command:
                self.lit.add(pos)

            if 'turn off' in command:
                if pos in self.lit:
                    self.lit.remove(pos)
