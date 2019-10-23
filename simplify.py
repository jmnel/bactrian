from .expression import Expression
from .expression import bractify
from .add import Add
from .mul import Mul
from .numeric_types import Numeric

def simplify(expr):

#    for i in range(0, len(expr.args)):
#        if hasattr(expr.args[i], 'args'):
#            expr.args[i] = simplify(expr.args[i])

    if issubclass(type(expr), Mul):
        non_numerics = []
        coef = 1
        for a in expr.args:
            if issubclass(type(a), Numeric):
                coef *= a.value
            else:
                non_numerics.append(a)

        lhs = (bractify(coef),)
        rhs = tuple(non_numerics)
        return Mul( lhs + rhs )

    elif issubclass(type(expr), Add):
        non_numerics = []
        coef = 0
        for a in expr.args:
            if issubclass(type(a), Numeric):
                coef += a.value
            else:
                non_numerics.append(a)

        lhs = (bractify(coef),)
        rhs = tuple(non_numerics)
        return Add( lhs + rhs )
