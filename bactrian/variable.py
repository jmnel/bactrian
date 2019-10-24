from .symbol import Symbol

class Variable(Symbol):
    def __init__(self, label):
        super(Variable, self).__init__(label)

    def __repr__(self):
        return '{}'.format( self.label )
