import sympy as sym
from variable import Variable

def is_scalar( expr ):
    return callable( getattr( expr , '__float__', False ) )

def is_variable( expr ):
    return type( expr ) is Variable

def parse_variable_times_scalar( expr ):
    if type( expr) is Variable:
        return 1.0, expr
    elif type( expr) is sym.Mul:
        if len( expr.args ) != 2:
            raise Exception('Failed to parse variable times scalar: wrong number of args')
        else:
            if is_scalar( expr.args[0] ) and is_variable( expr.args[1] ):
                return expr.args[0], expr.args[1]
            elif is_variable( expr.args[0] ) and is_scalar( expr.args[1] ):
                return expr.args[1], expr.args[0]
            else:
                raise Exception('Failed to parse variable times scalar')
    else:
        raise Exception('Failed to parse variable times scalar: wrong operator type')

def parse_linear_combination( expr ):

    root_is_variable_time_scalar = type( expr ) is sym.Mul
    if root_is_variable_time_scalar :
        coef, var = parse_variable_times_scalar( expr )
        return [[coef,var]]

    root_is_sum = type( expr ) is sym.Add

    if not root_is_sum: raise Exception( 'Failed to parse linear combination' )

    terms = []
    for term in expr.args:
        try:
            coef, var = parse_variable_times_scalar( term )
            terms.append( [ coef, var ] )
        except:
            raise Exception( 'Failed to parse linear combination term.' )

    return terms
