import re

class Grid:

    def __init__(self):
        self.lit = set()

    @property
    def lit_count(self):
        return len(self.lit)

    def act(self, command):
        x1, y1, x2, y2 = [int(i) for i in re.findall(r'\d+', command)]

        positions = [
            f'{x},{y}' for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)
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
