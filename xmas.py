class Grid:
    lit_count = 0

    def act(self, command):
        self.lit_count = 1 if 'turn on' in command else 0
