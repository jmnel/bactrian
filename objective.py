class Objective:
    def __init__( self, label, expr ):
        self.label = label
        self.expr = expr

    def __repr__(self):
        return '{}: {}'.format( self.label, self.expr )
