import re

class Grid:
    lit = set()

    @property
    def lit_count(self):
        return len(self.lit)

    def act(self, command):
        pos1, pos2 = re.search(r'.+(\d,\d) through (\d,\d)', command).groups()

        for pos in {pos1, pos2}:
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
