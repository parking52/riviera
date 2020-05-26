from game.configuration import player_health_point


class Player:

    def __init__(self, player_id):
        self.id = player_id
        self.player_health_point = player_health_point
        self.cards = []

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)