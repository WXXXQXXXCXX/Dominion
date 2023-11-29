import random

class Card:
    def __init__(self, name, cost, action=None):
        self.name = name
        self.cost = cost
        self.action = action

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.discard_pile = []

    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:
                self.shuffle_discard_into_deck()
            if self.deck:
                card = self.deck.pop()
                self.hand.append(card)

    def shuffle_discard_into_deck(self):
        random.shuffle(self.discard_pile)
        self.deck.extend(self.discard_pile)
        self.discard_pile = []

class DominionGame:
    def __init__(self, players):
        self.players = [Player(player_name) for player_name in players]
        self.supply = self.initialize_supply()

    def initialize_supply(self):
        # Define the supply of cards available in the game
        supply = {
            "Copper": Card("Copper", 0),
            "Silver": Card("Silver", 3),
            "Gold": Card("Gold", 6),
            "Estate": Card("Estate", 2),
            "Duchy": Card("Duchy", 5),
            "Province": Card("Province", 8),
        }
        return supply

    def play_turn(self, player):
        print(f"{player.name}'s turn:")
        player.draw_cards(5)
        print(f"Hand: {[card.name for card in player.hand]}")

        # Example: Buy a random card from the supply
        random_card_name = random.choice(list(self.supply.keys()))
        bought_card = self.supply[random_card_name]
        if bought_card.cost <= 0 or player.hand:
            player.hand.remove(bought_card)
            player.discard_pile.append(bought_card)
            print(f"{player.name} bought {bought_card.name}")

    def play_game(self):
        for _ in range(10):  # Let's say the game lasts for 10 turns
            for player in self.players:
                self.play_turn(player)


# Example usage:
players = ["Player1", "Player2"]
game = DominionGame(players)
game.play_game()
