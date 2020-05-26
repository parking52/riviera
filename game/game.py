import numpy as np
import math
import time
import random
from game.player import Player
from game.deck import Deck
from game.stack import Stack
from game.spell import Spell


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
            print('The following players are dead: ' + str(dead_players))
            self.clean_spells_to_and_from_dead_players(dead_players)

    def clean_spells_to_and_from_dead_players(self, dead_players):
        for player in dead_players:
            self.stack = [spell for spell in self.stack if spell.target != player or spell.origin != player]

    def resolve_stack(self):
        while len(self.stack) > 0:
            spell = self.stack.pop()
            spell.resolve()
            self.check_alive()

    def print_stacked_spell(self, spell):
        print('Stacked: a {type} spell from {player_origin} to {player_target}'.format(
            type=spell.type,
            player_origin=spell.origin,
            player_target=spell.target
        ))

    def print_game_stack(self):
        for spell in self.stack:
            print(spell)
