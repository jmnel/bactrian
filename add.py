from .expression import Expression

class Add(Expression):

    def __init__(self, args):
        from .expression import bractify
        new_args = []
        for a in args:
            if type( a ) is Add:
                for a_child in a.args:
                    new_args.append( a_child )
            else:
                new_args.append( a )
        self.args = tuple( bractify(e) for e in new_args )

    def __repr__(self):
        str = ''
        str += '{}'.format( self.args[0] )
        for i in range(1,len(self.args)):
            str += ' + {}'.format( self.args[i] )

        return str


#from .numeric_types import Float
