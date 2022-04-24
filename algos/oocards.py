import random


class Deck:
    def __init__(self, contents, aces_high=True, jokers=False, name="Unnamed Deck"):
        self.contents = contents
        self.jokers = jokers
        self.name = name
        self.aces_high = aces_high
        self.index = 0
        self.suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        self.values = {"Ace": 14, "One": 1, "Two": 2, "Three": 3, "Four": 4,
                       "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                       "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}

        if self.jokers:
            self.values["Joker"] = 15

        if not self.aces_high:
            self.values["Ace"] = 0
            for val in self.values:
                self.values[val] = self.values[val] + 1

        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def deal(self, deck):
        if self.contents:
            deck.add_card(self.contents[0])
            self.remove_card(self.contents[0])

    def __next__(self):
        if len(self.contents) > self.index:
            item = self.contents[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.contents[item]

    def __repr__(self):
        return self.name + ": " + str(self.contents)

    def add_card(self, c):
        if type(c) == Card:
            self.contents.append(c)
            if c.deck:
                c.deck.remove_card(c)
            c.deck = self

    def remove_card(self, c):
        if type(c) == Card:
            for i, item in enumerate(self.contents):
                if c == item:
                    c.deck = None
                    del self.contents[i]
        elif type(c) == str:
            for i, item in enumerate(self.contents):
                if item.full == c.full:
                    c.deck = None
                    del self.contents[i]

    def setup(self, content=None):
        if content:
            # make it so you can setup custom decks
            pass
        else:
            for suit in self.suits:
                for card in self.values:
                    if card != "Joker":
                        c = Card(card, suit, self)
                        self.add_card(c)
            if self.jokers:
                self.add_card(Card("Joker", "", self, True))
                self.add_card(Card("Joker", "", self, True))

    def shuffle(self, method="", num=None):
        if not num:
            num = 3
        if "riffle" in method:
            pass
        if "overhand" in method:
            usable_range = range(round(len(self.contents)/8), round(len(self.contents) * 7 / 8))
            for _ in range(num):
                start = random.choice(usable_range)
                self.cut(start)
        if not method:
            for _ in range(num):
                con = self.contents
                random.shuffle(con)
                self.contents = con

    def cut(self, index=26):
        half1 = self.contents[0:index]
        half2 = self.contents[index-1:-1]
        self.contents = half2 + half1

    def top(self):
        return self.contents[0]

    def bottom(self):
        return self.contents[-1]


class Card:
    def __init__(self, name, suit, deck=None, joker=False):
        if not joker:
            self.name = name
            self.suit = suit
            self.full = self.name + " of " + self.suit\

        else:
            self.name = "Joker"
            self.suit = None
            self.full = "Joker"

        self.value = deck.values[self.name]
        self.deck = deck

    def __str__(self):
        return self.full

    def __repr__(self):
        return self.full

    def __int__(self):
        return self.value


if __name__ == "__main__":
    d = Deck([])
    d.setup()
    d.shuffle()

    amount = 2
    players = []

    while amount > 0:
        temp = Deck([], name="p" + str(amount))
        players.append(temp)
        amount -= 1

    length = len(d.contents)

    while length > 0:
        d.deal(players[length % 2])
        length -= 1

    while True:
        if len(players) == 1:
            break
        # 1 turn simple logic
        tops = [player.top() for player in players]
        p_n = players
        top_val = 0
        winners, t_cards, cards = [], [], []

        for x in tops:
            cards.append(x)
            if x.value > top_val:
                top_val = x.value

        for x in tops:
            if x.value == top_val:
                winners.append(x)

        if len(winners) > 1:
            # if there is a war
            pass

        for card in cards:
            winners[0].add_card(card)

        for x in p_n:
            if not x.contents:
                players.remove(x)
