class Deck:

    def __init__(self):
        self.cards = ['A', 'K', 4, 7]
    
    def __repr__(self) -> str:
        return f"{self.__dict__}"
    
    def __getitem__(self, key):
        return self.cards[key]
    
    def __len__(self):
        return len(self.cards)
    

deck = Deck()

print(deck.__getitem__(1))

print(deck.__len__())