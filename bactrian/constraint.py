from .expression import Expression

class Constraint:
    def __init__(self, label: str, expr: Expression):
        from .numeric_types import Numeric
        from .relation import Relation
        from .label import validate_label

        expr_is_relation = isinstance(expr, Relation)
        if not expr_is_relation:
            raise TypeError('Constructing Constraint failed: \"%s\" is not type Relation'
                    % str(expr))

        if not isinstance(expr.rhs(), Numeric):
            raise Exception('Constructing Constraint failed: rhs \"%s\" is not numeric type'
                    % str(expr.rhs()))

        self.label = validate_label(label)
        self.expr = expr

    def __repr__(self):
        return('%s: %s' % (self.label, str(self.expr)))
