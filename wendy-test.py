import random

class DominionGame:
    def __init__(self):
        self.players = []
        self.supply = {
            'copper': 60,
            'silver': 40,
            'gold': 30,
            'estate': 8,
            'duchy': 8,
            'province': 8,
        }
        self.player_deck = {}
        self.player_hand = {}
        self.player_discard = {}

    def add_player(self, player_name):
        self.players.append(player_name)
        self.player_deck[player_name] = ['copper'] * 7 + ['estate'] * 3
        random.shuffle(self.player_deck[player_name])
        self.player_hand[player_name] = []
        self.player_discard[player_name] = []

    def draw_cards(self, player_name, num_cards):
        while len(self.player_hand[player_name]) < num_cards:
            if len(self.player_deck[player_name]) == 0:
                self.player_deck[player_name] = self.player_discard[player_name]
                self.player_discard[player_name] = []
                random.shuffle(self.player_deck[player_name])
            self.player_hand[player_name].append(self.player_deck[player_name].pop(0))

    def play_action_phase(self, player_name):
        actions_played = 0
        while actions_played < 1:  # Limiting to 1 action for simplicity
            # Check if the player has any action cards in hand
            action_cards = [card for card in self.player_hand[player_name] if card == 'village']  # Add more action cards
            if not action_cards:
                break  # No action cards left to play

            # Play an action card (in this example, just playing a 'Village' card)
            card_index = self.player_hand[player_name].index('village')  # Index of the action card
            played_card = self.player_hand[player_name].pop(card_index)  # Remove the card from hand
            print(f"{player_name} plays {played_card}")
            actions_played += 1

            # Additional game logic based on the action card played would go here

    def play_turn(self, player_name):
        self.draw_cards(player_name, 5)
        self.play_action_phase(player_name)
        # Additional phases of a turn (Buy Phase, Clean-up) would go here

    def print_player_info(self, player_name):
        print(f"Player: {player_name}")
        print(f"Hand: {', '.join(self.player_hand[player_name])}")
        print(f"Deck count: {len(self.player_deck[player_name])}")
        print(f"Discard count: {len(self.player_discard[player_name])}")
        print("\n")

    def calculate_buying_power(self, player_name):
        # Count the total value of treasure cards in the player's hand
        treasure_values = {'copper': 1, 'silver': 2, 'gold': 3}
        return sum(treasure_values[card] for card in self.player_hand[player_name] if card in treasure_values)

    def buy_cards(self, player_name):
        buying_power = self.calculate_buying_power(player_name)
        while buying_power > 0:
            # Example: Let the player buy a card of their choice that they can afford
            chosen_card = input(f"{player_name}, choose a card to buy (or 'pass'): ")
            if chosen_card == 'pass':
                break
            if chosen_card in self.supply and self.supply[chosen_card] > 0 and treasure_values[chosen_card] <= buying_power:
                self.supply[chosen_card] -= 1
                self.player_discard[player_name].append(chosen_card)
                buying_power -= treasure_values[chosen_card]
            else:
                print("Invalid choice. Try again.")

    def play_turn(self, player_name):
        self.draw_cards(player_name, 5)
        self.play_action_phase(player_name)
        self.buy_cards(player_name)  # Added buy phase
        self.clean_up(player_name)  # Assuming clean_up is implemented


# Usage example:
if __name__ == "__main__":
    game = DominionGame()
    game.add_player('Player 1')
    game.add_player('Player 2')

    for player in game.players:
        game.play_turn(player)
        game.print_player_info(player)
