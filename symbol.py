from .expression import Expression

class Symbol(Expression):
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return '{}'.format( self.label )

