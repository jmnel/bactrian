from .expression import Expression

class Mul(Expression):
    def __init__(self, args):
        from .expression import bractify
        new_args = []
        for a in args:
            if type( a ) is Mul:
                for a_child in a.args:
                    new_args.append( a_child )
            else:
                new_args.append( a )
        self.args = tuple( bractify(e) for e in new_args )

    def __repr__(self):
        from .add import Add
        str = ''
        for i in range(0,len(self.args)):
            a = self.args[i]
            if type( a ) is Add:
                str += '( {} )'.format(a)
            else:
                str += '{}'.format( a )

            if i + 1 < len( self.args ):
                str += ' * '

        return str
