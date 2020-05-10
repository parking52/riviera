class Spell:

    def __init__(self, id, origin, target, type='red'):
        self.id = id
        self.origin = origin
        self.target = target
        self.type = type

    def resolve(self):

        self.target.player_health_point -= 1

    def resolve_any_spell(self, players):
        pass

    def __repr__(self):
        return 'TO BE IMPLEMENTED'

    def __str__(self):
        return 'TO BE IMPLEMENTED'
