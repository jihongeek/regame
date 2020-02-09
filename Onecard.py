import random
deck = [] 
cardsymbol = ["spade","clover","diamond","heart"]
cardnum = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in cardsymbol:
    for j in cardnum:
        deck.append((i,j)) 
for i in range(0,2):
    deck.append("joker")
random.shuffle(deck)
class Player:
    def __init__(self,playername):
        self.cards = {"spade":[],"clover":[],"diamond":[],"heart":[]}
        self.name = playername
    def getcard(self,deck):
        self.cards[deck[0][0]].append(deck[0][1])
        deck.remove(deck[0]) 
p1 = Player("jihongkim")
p1.getcard(deck)
print(p1.cards,deck)