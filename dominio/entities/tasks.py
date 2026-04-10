class Task:
    def __init__(self, name, checked=False):
        self.name = name
        self.checked = checked

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def toggle(self):
        self.checked = not self.checked