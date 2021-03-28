# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


class Influence(object):
    characters = ['ambassador', 'assassin', 'captain', 'contessa', 'duke']

    def __init__(self, name):
        assert name in self.characters
        self.name = name
        self.revealed = False


class Player(object):

    def __init__(self, name, coins, game):
        self.coins = coins
        self.name = name
        self.influence = [game.influence_deck.pop(), game.influence_deck.pop()]


class Game(object):

    def __init__(self, player_names):
        self.influence_deck = [Influence(name) for name in Influence.characters] * 3
        random.shuffle(self.influence_deck)
        self.initial_coins = 2 if len(player_names) > 2 else 1
        self.players = [Player(name, self.initial_coins, self) for name in player_names]


def new_game():
    player_1_name = input("Welcome to Coup! What should we call you?\n")
    player_names = [player_1_name]
    for i in range(5):
        next_name = input("What's the next player's name?\n")
        player_names.append(next_name)
        if i != 4:
            all_players_set = input("Is that all the players?\n")
            if all_players_set[:1].lower() == 'y':
                break
    return Game(player_names)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = new_game()
    import pdb
    pdb.set_trace()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
