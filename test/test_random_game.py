import numpy as np
import math
import time
import random
from game.game import Game
from game.player import Player
from game.deck import Deck
from game.stack import Stack
from game.spell import Spell


if __name__ == '__main__':

    players = [Player(player_id=i) for i in range(4)]
    game = Game(players)

    unique_spell_id = 0

    while game.n_players_alive > 1:

        for i in range(4):
            spell = Spell(id=unique_spell_id, origin=random.choice(game.players_alive), target=random.choice(game.players_alive))
            game.print_stacked_spell(spell)
            game.stack.append(spell)

        unique_spell_id += 1

        while len(game.stack) > 0:
            print('current stack')
            game.print_game_stack()
            #offer_play(player)
            #count_no_actions += 1
            count_no_actions = 1000

            if count_no_actions > game.n_players_alive:
                #count_no_actions = 0
                game.resolve_stack()

        print("There is " + str(game.n_players_alive) + " players alive")
        time.sleep(2)
        game.check_alive()

    print('game over, winner is ' + str(game.players_alive[0].id))
