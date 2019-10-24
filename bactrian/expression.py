def bractify(arg):
    from .numeric_types import Float, Integer
    if isinstance(arg, float):
        return Float(arg)
    if isinstance(arg, int):
        return Integer(arg)
    else:
        return arg

class Expression:
    def __init__(self):
        pass

    def __mul__(self, rhs):
        return Mul(self, rhs)

    def __rmul__(self, lhs):
        return Mul(lhs, self)

    def __add__(self, rhs):
        return Add(self, rhs)

    def __radd__(self, lhs):
        return Add(rhs, self)

    def __sub__(self, rhs):
        return Add(self, Mul(-1, rhs))

    def __rsub__(self, lhs):
        return Add(Mul(-1, lhs), self)

    def __neg__(self):
        return Mul(-1, self)

    def __lt__(self, rhs):
        from .relation import LessThanStrict
        return LessThanStrict(self, rhs)

    def __gt__(self, rhs):
        from .relation import GreaterThanStrict
        return GreaterThanStrict(self, rhs)

    def __le__(self, rhs):
        from .relation import LessThan
        return LessThan(self, rhs)

    def __ge__(self, rhs):
        from .relation import GreaterThan
        return GreaterThan(self, rhs)

    def __eq__(self, rhs):
        from .relation import EqualTo
        return EqualTo(self, rhs)

    def __ne__(self, rhs):
        from .relation import NotEqualTo
        return NotEqualTo(self, rhs)

def parse_symbol_times_scalar(expr):
    from .symbol import Symbol
    if (not isinstance(expr, Mul)) and (not isinstance(expr, Symbol)):
        raise TypeError('Failed to parse expression: \"%s\" must be type Mul or Symbol' 
                % str(expr))

    if isinstance(expr, Symbol):
        return (1, expr)

    is__symbol = list(map(lambda a : isinstance(a, Symbol), expr.args))
    is__numeric = list(map(lambda a : isinstance(a, Numeric), expr.args))

    symbol_count = is__symbol.count(True)
    numeric_count = is__symbol.count(True)

    if symbol_count != 1:
        # Should these 2 exceptions be TypeError instead?
        raise ValueError('Failed to parse expression: \"%s\" must contain exactly one of type Smybol'
                % str(expr))

    if numeric_count != len(expr.args)-1:
        raise ValueError('Failed to parse expression: \"%s\" must contain n-1 of type Numeric'
                % str(expr))

    coef, symb = 1, None
    for i, arg in enumerate(expr.args):
        if is_symbol[i]:
            assert (not is_numeric[i]), ('not is_numeric[%d]' % i))
            symb = arg
        else:
            assert is_numeric[i] ('is_numeric[%d]' % i)
            coef *= arg.value
    return (coef, symb)

def parse_linear_combination(expr):
    from .symbol import Symbol
    if isinstance(expr, Symbol):
        return [(1, expr)]
    if isinstance(expr, Mul):
        return [parse_symbol_times_scalar(expr)]
    elif isinstance(expr, Add):
        return [parse_symbol_times_scalar(t) for t in expr.args]
    else:
        raise TypeError('Failed to parse linear combination: \"%s\" is not type Add or Mul'
                % str(expr))


from .add import Add
from .mul import Mul
