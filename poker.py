"""
Author: John Doan
Module for Homework 5, Problem 1
Object Oriented Programming (50:198:113), Fall 2021

A module to simulate cards and poker hands in a standard deck. 
"""

class Card:
    """
    An instance of the class defines a standard playing card
    with a suit and a face value. 
    """
    allsuits = 'CDHS'
    allfaces = '23456789TJQKA'

    def __init__(self, csuit, cface):
        """
        Initialize the card's suit and face value

        csuit - a character in 'CDHS'
        cface - a character in '23456789TJQKA'
        """
        if csuit not in Card.allsuits or cface not in Card.allfaces:
            raise Exception("Error: Invalid Card object")
        self.suit = csuit
        self.face = cface

    # --------------------------------------------------------
    # COMPLETE THE REST of the Card class implementation below
    # --------------------------------------------------------    

    def str(self):
        return str(self.suit + self.face)
        
    def eq(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 == hand2

    def ne(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 != hand2

    def __lt__(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 < hand2

    def __le__(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 <= hand2

    def __gt__(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 > hand2
        
    def __ge__(self, other):
        hand1 = self.suit, self.face
        hand2 = other.suit, other.face
        return hand1 >= hand2

class CardDeck:
    """
    A class that represents a deck of cards. The deck starts
    out as a standard 52-card deck but will have fewer cards if
    some cards have been dealt out. 
    """

    # --------------------------------------------------------    
    # COMPLETE the CardDeck class implementation below
    # --------------------------------------------------------
    
    def __init__(self):
        list_suit = list(Card.allsuits)
        list_face = list(Card.allfaces)
        self._deck = []
        for suits in list_suit:
            for face in list_face:
                card = "{}{}".format(suits, face)
                self._deck.append(card)

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return str(self._deck)

    def __iter__(self):
        return self

    def deal(self):
        return self._deck.pop(0)

    def shuffle(self):
        import random
        num_cards = len(self._deck)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self._deck[i], self._deck[j] = self._deck[j], self._deck[i]

class CardDeckIterator:
    def __init__(self, max=52):
        self.max = max

    def __next__(self):
        count = 0
        if count < self.max:
            count += 1
            return CardDeck.__iter__()
        else:
            raise StopIteration

class PokerHand:
    """
    A five card poker hand. The hands in decreasing order of
    rank are 'Straight Flush', 'Four Of A Kind', 'Full House',
    'Flush', 'Straight', 'Three Of A Kind', 'Two Pair', 'One Pair',
    and 'High Card'
    """
    numcards = 5
    handtypes = ['Straight Flush', 'Four Of A Kind',
                 'Full House', 'Flush', 'Straight', 
                 'Three Of A Kind', 'Two Pair', 'One Pair', 
                 'High Card']

    # -------------------------------------------------------------    
    # COMPLETE THE REST of the PokerHand class implementation below
    # -------------------------------------------------------------    
        
    def __init__(self, deck):
        self.cards = []
        self.suitcounts = {'C':0, 'D': 0, 'H':0, 'S': 0}
        self.facecounts = {'2': 0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0,
                           '9': 0,'T': 0, 'J': 0, 'Q': 0, 'K':0, 'A': 0}

        i = 0
        while i < PokerHand.numcards:
            self.cards.append(deck.deal())                  
            i += 1
        print(self.cards)

        for x in self.cards:
            if x[1:] in self.facecounts:
                self.facecounts[x[1:]] += 1
            if x[:1] in self.suitcounts:
                self.suitcounts[x[:1]] += 1

    def __str__(self):
        return str(self.cards)

    def checkIfInSequeuce(sortedCard):
        left, right = 0, 1
        list_face = list(Card.allfaces)
        while right < len(sortedCard):
            leftCard, rightCard = sortedCard[left], sortedCard[right]
            leftKind, rightKind = leftCard[1:], rightCard[1:]
            different = list_face.index(leftKind) - list_face.index(rightKind)

            if (different > 0): 
                if different % (len(list_face) - 2) != -1:
                    return False
            elif (different != -1 and different != -9): # -9 here for case Ace -> 5
                return False
                
            left, right = left + 1, right + 1

        return True

    def evaluate(self):
        if PokerHand.isStraightFlush(self) == True:
            return PokerHand.handtypes[0]
        elif PokerHand.isFourOfAKind(self) == True:
            return PokerHand.handtypes[1]
        elif PokerHand.isFullHouse(self) == True:
            return PokerHand.handtypes[2]
        elif PokerHand.isFlush(self) == True:
            return PokerHand.handtypes[3]
        elif PokerHand.isStraight(self) == True:
            return PokerHand.handtypes[4]
        elif PokerHand.isThreeOfAKind(self) == True:
            return PokerHand.handtypes[5]
        elif PokerHand.isTwoPair(self) == True:
            return PokerHand.handtypes[6]
        elif PokerHand.isOnePair(self) == True:
            return PokerHand.handtypes[7]
        else:
            return PokerHand.handtypes[8]

    def isStraightFlush(self):
        if (5 in self.suitcounts.values() and PokerHand.checkIfInSequeuce(self.cards)):
            return True
        else:
            return False

    def isFourOfAKind(self):
        if 4 in self.facecounts.values():
            return True
        else:
            return False
            
    def isFullHouse(self):
        if (3 in self.facecounts.values()) and (2 in self.facecounts.values()):
            return True
        else:
            return False

    def isFlush(self):
        if (5 in self.suitcounts.values() and not PokerHand.checkIfInSequeuce(self.cards)):
            return True
        else:
            return False

    def isStraight(self):
        validSuit = (2 in self.suitcounts.values() or 3 in self.suitcounts.values() or 4 in self.suitcounts.values() or 5 in self.suitcounts.values())
        if (PokerHand.checkIfInSequeuce(self.cards) and validSuit):
            return True
        else:
            return False
            
    def isThreeOfAKind(self):
        if 3 in self.facecounts.values():
            return True
        else:
            return False

    def isTwoPair(self):
        totalTwoPairsCount = 0
        for numberOfKindFound in self.facecounts.values():
            if numberOfKindFound == 2:
                totalTwoPairsCount += 1
            if (totalTwoPairsCount == 2):
                return True
            else:
                return False
        
    def isOnePair(self):
        if 2 in self.facecounts.values():
            return True
        else:
            return False

if __name__=="__main__":
    print("---------------------------------------------------")
    print("Testing Problem 1, Homework 5\n")
    print("This is pretty basic test code. Feel free to add more")
    print("test code to demonstrate that your PokerHand class ")
    print("implementation works correctly!")
    print("---------------------------------------------------")    
    myDeck = CardDeck()
    print("Standard Deck: "+str(myDeck))
    print("Dealing 5 cards.....")
    hand = PokerHand(myDeck)      # top 5 cards from deck
    print("Sorted Hand: "+str(hand))
    print("Best Rank: %s"%hand.evaluate())

    print("\nA straight flush is no surprise since we didn't shuffle the deck yet!")
    print("We will shuffle the deck once and deal a few more hands....\n")
    myDeck.shuffle()
    print("Shuffled Deck: "+str(myDeck))
    print("")
    
    for i in range(3):
        print("Dealing 5 cards.....")
        hand = PokerHand(myDeck)      # top 5 cards from deck
        print("Sorted Hand: "+str(hand))
        print("Best Rank: %s"%hand.evaluate())
        print("")

    print("Shuffling the deck again....")
    myDeck.shuffle()
    print("Shuffled Deck: "+str(myDeck))
    print("")
    
    for i in range(3):
        print("Dealing 5 cards.....")
        hand = PokerHand(myDeck)      # top 5 cards from deck
        print("Sorted Hand: "+str(hand))
        print("Best Rank: %s"%hand.evaluate())
        print("")
