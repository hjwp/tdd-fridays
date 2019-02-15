import re

class Grid:
    lit = set()

    @property
    def lit_count(self):
        return len(self.lit)

    def act(self, command):
        pos = re.search(r'.+(\d,\d).+', command).group(1)

        if 'toggle' in command:
            if pos in self.lit:
                self.lit.remove(pos)
            else:
                self.lit.add(pos)

        if 'turn on' in command:
            self.lit.add(pos)

        if 'turn off' in command:
            try:
                self.lit.remove(pos)
            except KeyError:
                pass
