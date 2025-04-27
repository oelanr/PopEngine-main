class Population:
    def __init__(self, initial_count: int):
        self.initial_count = initial_count
        self.values = []

    def reset(self):
        self.values = [self.initial_count]

    def update(self, new_value):
        self.values.append(new_value)

    def current(self):
        return self.values[-1] if self.values else self.initial_count
