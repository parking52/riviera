class Stack:

    def __init__(self, origin, target, type):
        self.origin = origin
        self.target = target
        self.type = type

    def resolve_any_spell(self):

        self.target.player_health_point -= 1

    def __repr__(self):
        return 'TO BE IMPLEMENTED'

    def __str__(self):
        return 'TO BE IMPLEMENTED'
