class Grid:
    lit_count = 0

    def act(self, command):
        if 'toggle' in command:
            self.lit_count = 1 if self.lit_count == 0 else 0
        if 'turn on' in command:
            self.lit_count = 1
        if 'turn off' in command:
            self.lit_count = 0

