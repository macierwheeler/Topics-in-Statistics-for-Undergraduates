# Macie Wheeler
# Project 12

### Question 1

class Card:
    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 14}
    def __init__(self, number, suit):
      self.number = number
      self.suit = suit
      
      if number not in {2,3,4,5,6,7,8,9,10}:
        if number not in {"2", "3", "4", "5", "6", "7", "8", "9", "10"}:
          if number not in {"j", "q", "k", "a"}:
            if number not in {"J", "Q", "K", "A"}:
              raise Exception("Number wasn't 2-10 or J, Q, K, or A.")
      else:
        self.number = str(self.number)
      
      if suit.lower() not in {"clubs", "hearts", "spades", "diamonds"}:
        raise Exception("Suit wasn't one of: clubs, hearts, spades, or diamonds.")
      else:
        self.suit = suit.lower()


my_card = Card(11, "Hearts") # Exception: Number wasn't 2-10 or J, Q, K, or A.
my_card = Card(10, "Stars") # Suit wasn't one of: clubs, hearts, spades, or diamonds.
my_card = Card("10", "Spades")
my_card = Card("2", "clubs")
my_card = Card("2", "club") # Suit wasn't one of: clubs, hearts, spades, or diamonds.

### Question 2

class Card:
    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 14}
    def __init__(self, number, suit):
      self.number = number
      self.suit = suit
      
      if number not in {2,3,4,5,6,7,8,9,10}:
        if number not in {"2", "3", "4", "5", "6", "7", "8", "9", "10"}:
          if number not in {"j", "q", "k", "a"}:
            if number not in {"J", "Q", "K", "A"}:
              raise Exception("Number wasn't 2-10 or J, Q, K, or A.")
      else:
        self.number = str(self.number)
      
      if suit.lower() not in {"clubs", "hearts", "spades", "diamonds"}:
        raise Exception("Suit wasn't one of: clubs, hearts, spades, or diamonds.")
      else:
        self.suit = suit.lower()
        
    def __str__(self):
      return(f'{self.number} of {self.suit}')
      
    def __repr__(self):
      return(f'{self.__class__.__name__}(str({self.number}), "{self.suit}")')


print(Card("10", "Spades")) # 10 of spades
print(Card("2", "clubs")) # 2 of clubs
repr(Card("10", "Spades")) # Card(str(10), "spades")
repr(Card("2", "clubs")) # Card(str(2), "clubs")

### Question 3

class Card:
    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 14}
    def __init__(self, number, suit):
      self.number = number
      self.suit = suit
      
      if number not in {2,3,4,5,6,7,8,9,10}:
        if number not in {"2", "3", "4", "5", "6", "7", "8", "9", "10"}:
          if number not in {"j", "q", "k", "a"}:
            if number not in {"J", "Q", "K", "A"}:
              raise Exception("Number wasn't 2-10 or J, Q, K, or A.")
      else:
        self.number = str(self.number)
      
      if suit.lower() not in {"clubs", "hearts", "spades", "diamonds"}:
        raise Exception("Suit wasn't one of: clubs, hearts, spades, or diamonds.")
      else:
        self.suit = suit.lower()
        
    def __str__(self):
      return(f'{self.number} of {self.suit}')
      
    def __repr__(self):
      return(f'{self.__class__.__name__}(str({self.number}), "{self.suit}")')
      
    def __eq__(self, other):
      if self.number == other.number:
        return True
      else:
        return False
      
    def __lt__(self, other):
      v_dict = {"j": 11, "q": 12, "k": 13, "a": 14}
      
      if self.number in {'j', 'q', 'k', 'a'} or self.number in {'J', 'Q', 'K', 'A'}:
        self.number = int(v_dict[self.number.lower()])
      
      if other.number in {'j', 'q', 'k', 'a'} or other.number in {'J', 'Q', 'K', 'A'}:
        other.number = int(v_dict[other.number.lower()])
      
      if int(self.number) < int(other.number):
        return True
      else:
        return False
      
    def __gt__(self, other):
      v_dict = {"j": 11, "q": 12, "k": 13, "a": 14}
      
      if self.number in {'j', 'q', 'k', 'a'} or self.number in {'J', 'Q', 'K', 'A'}:
        self.number = int(v_dict[self.number.lower()])
      
      if other.number in {'j', 'q', 'k', 'a'} or other.number in {'J', 'Q', 'K', 'A'}:
        other.number = int(v_dict[other.number.lower()])
      
      if int(self.number) > int(other.number):
        return True
      else:
        return False


card1 = Card(2, "spades")
card2 = Card(3, "hearts")
card3 = Card(3, "diamonds")
card4 = Card(3, "Hearts")
card5 = Card("A", "Spades")
card6 = Card("A", "Hearts")
card7 = Card("K", "Diamonds")

print(card1 < card2) # True
print(card1 < card3) # True
print(card2 == card3) # True
print(card2 == card4) # True
print(card3 < card4) # False
print(card4 < card3) # False
print(card5 > card4) # True
print(card5 > card6) # False
print(card5 == card6) # True
print(card7 < card5) # True
print(card7 > card1) # True

### Question 4

class Deck:
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]
        

lucky_deck = Deck()
print(lucky_deck)
print(len(lucky_deck))
print(lucky_deck[10])

# If I try to print the length of the Deck it says that a Deck object has no
# attribute len().
# If I try to print a single card from the Deck it says that a Deck object is 
# not subscriptable.

### Question 5

class Deck:
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")
    
    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]
    
    def __len__(self):
      return len(self.cards)
      
    def __getitem__(self, index):
      return self.cards[index]
        

lucky_deck = Deck()
len(lucky_deck) # 52
print(lucky_deck[10]) # q of clubs 
