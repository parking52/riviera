import numpy as np
import math
import time
import random
from player import Player
from deck import Deck
from stack import Stack
from spell import Spell


class Game:

    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.stack = []
        self.players_alive = players
        self.n_players_alive = len(self.players_alive)
        self.check_alive()

    def check_alive(self):
        temp = self.players_alive
        self.players_alive = [player for player in self.players if player.player_health_point > 0]
        self.n_players_alive = len(self.players_alive)
        dead_players = set(temp) - set(self.players_alive)
        if dead_players:
            print('The following players are dead' + str(dead_players))
            self.clean_spells_to_and_from_dead_players(dead_players)


    def clean_spells_to_and_from_dead_players(self, dead_players):
        for player in dead_players:
            game.stack = [spell for spell in game.stack if spell.target != player or spell.origin != player]




    def resolve_stack(self):
        while len(self.stack) > 0:
            spell = self.stack.pop()
            spell.resolve()
            game.check_alive()

    def print_stacked_spell(self, spell):
        print('Stacked: a {type} spell from {player_origin} to {player_target}'.format(
            type=spell.type,
            player_origin=spell.origin,
            player_target=spell.target
        ))


if __name__ == '__main__':

    players = [Player(player_id=i) for i in range(4)]
    game = Game(players)

    unique_spell_id = 0

    while game.n_players_alive > 1:

        spell = Spell(id=unique_spell_id, origin=players[random.randint(0, 3)], target=players[random.randint(0, 3)],)
        game.print_stacked_spell(spell)
        game.stack.append(spell)
        unique_spell_id += 1

        while len(game.stack) > 0:
            print('current stack')
            print(game.stack)
            #offer_play(player)
            #count_no_actions += 1
            count_no_actions = 1000

            if count_no_actions > game.n_players_alive:
                #count_no_actions = 0
                game.resolve_stack()

        print(game.n_players_alive)
        time.sleep(2)
        game.check_alive()

    print('game over, winner is')
