from .expression import Expression, bractify

def simplify(expr):
    from .add import Add
    from .mul import Mul
    from .numeric_types import Numeric

    if isinstance(expr, Mul):
        non_numerics = list()
        coef = 1
        for a in expr.args:
            if isinstance(a, Numeric):
                coef *= a.value
            else:
                non_numerics.append(a)

        lhs = (bractify(coef), )
        rhs = tuple(non_numerics)
        return Mul(lhs + rhs)

    elif isinstance(expr, Add):
        non_numerics = list()
        coef = 0
        for a in expr.args:
            if isinstance(a, Numeric):
                coef += a.value
            else:
                non_numerics.append(a)

        lhs = (bractify(coef), )
        rhs = tuple(non_numerics)
        return Add(lhs + rhs)
    else:
        return expr
