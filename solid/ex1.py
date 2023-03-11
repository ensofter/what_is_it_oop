class Journal:

    def __init__(self):
        self.entries: list = []
        self.count: int = 0

    def add_entry(self, text: str = None):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.count[pos]

    def __str__(self):
        return '\n'.join(self.entries)


if __name__ == '__main__':
    j = Journal()
    j.add_entry("I fulfill today review")
    j.add_entry("I rewrite today mocks")

    print(f'Journal entries: \n{j}')
