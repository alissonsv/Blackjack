class Card():
    def set_value(self):
        if self.rank in ['JACK', 'QUEEN', 'KING']:
            self.value = 10
        elif self.rank == 'Ace':
            self.value = 11
        else:
            self.value = int(self.rank)

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.set_value()

    def __str__(self):
        return f"{self.rank} of {self.suit}"
