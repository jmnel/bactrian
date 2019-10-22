def bractify(arg):
    if type( arg ) is float:
        return Float(arg)
    if type( arg ) is int:
        return Integer(arg)
    else:
        return arg

class Expression:
    def __init__(self):
        foo = 5

    def __mul__( self, rhs ):
        return Mul( ( self, rhs ) )

    def __rmul__( self, rhs ):
        return Mul( ( rhs, self ) )

    def __add__( self, rhs ):
        return Add( ( self, rhs ) )

    def __radd__( self, rhs ):
        return Add( ( rhs, self ) )

    def __sub__( self, rhs ):
        return Add( ( self, Mul( ( -1, rhs ) ) ) )

    def __rsub__( self, rhs ):
        return Add( ( Mul( ( -1, rhs ) ) ), self )

    def __lt__( self, rhs ):
        from .relation import LessThanStrict
        return LessThanStrict( self, rhs )

    def __gt__( self, rhs ):
        from .relation import GreaterThanStrict
        return GreaterThanStrict( self, rhs )

    def __le__( self, rhs ):
        from .relation import LessThan
        return LessThan( self, rhs )

    def __ge__( self, rhs ):
        from .relation import GreaterThan
        return GreaterThan( self, rhs )

    def __eq__( self, rhs ):
        from .relation import EqualTo
        return EqualTo( self, rhs )

    def __ne__( self, rhs ):
        from .relation import NotEqualTo
        return NotEqualTo( self, rhs )

def parse_symbol_times_scalar( expr ):
    from .symbol import Symbol
    if not type( expr ) is Mul and not issubclass( type( expr ), Symbol ):
        raise Exception( 'Failed to parse expression: "{}" must be type Mul or Symbol'.format( expr ) )

    if issubclass( type( expr ), Symbol ) :
        return [ 1, expr ]
    elif issubclass( type( expr.args[0] ), Numeric ) and  issubclass( type( expr.args[1] ), Symbol ):
        coef = expr.args[0]
        symb = expr.args[1]
        return coef, symb
    elif issubclass( type( expr.args[0] ), Symbol ) and issubclass( type( expr.args[1] ), Numeric ):
#    elif type( expr.args[0] ) is Symbol and type( expr.args[1] ) is Numeric:
        coef = expr.args[1]
        symb = expr.args[0]
        return coef, symb
    else:
        raise Exception( 'Failed to parse expresion: "{}" does not match symbol times scalar pattern'
                .format( expr ) )


def parse_linear_combination( expr ):

    if type( expr ) is Mul:
        return [ parse_symbol_times_scalar( expr ) ]
    elif type( expr ) is Add:
        terms = []
        for t in expr.args:
            terms.append( parse_symbol_times_scalar( t ) )

        return terms
    else:
        raise Exception( 'Failed to parse linear combination: "{}" is not type Add or Mul'
                .format( expr ) )


from .add import Add
from .mul import Mul
from .numeric_types import Numeric
from .numeric_types import Float
from .numeric_types import Integer
#from .relation import LessThan
#from .relation import LessThanStrict
#from .relation import GreaterThan
#from .relation import GreaterThanStrict
#from .relation import EqualTo
