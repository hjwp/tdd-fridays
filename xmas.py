class Grid:
    lit_count = 0

    def act(self, command):
        self.lit_count = 1 if not 'toggle' in command else 0
