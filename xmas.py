class Grid:
    lit_count = 0
    history = []

    def act(self, command):
        if command in self.history:
            return

        history.append(command)

        if 'toggle' in command:
            self.lit_count = 1 if self.lit_count == 0 else 0
        if 'turn on' in command:
            self.lit_count += 1
        if 'turn off' in command:
            self.lit_count -= 1 if not self.lit_count == 0 else 0
