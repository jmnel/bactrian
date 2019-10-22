from .relation import Relation

class Constraint:
    def __init__( self, label, expr ):

        from .numeric_types import Numeric

        expr_is_relation = issubclass( type( expr ), Relation )
        if not expr_is_relation:
            raise Exception( 'Constructing Constraint failed: "{}" is not type Relation'
                    .format( expr ) )

        if not issubclass( type( expr.rhs() ), Numeric ):
            raise Exception( 'Constructing Constraint failed: rhs "{}" is not numeric type'
                    .format( expr.rhs() ) )

        self.label = label
        self.expr = expr

    def __repr__(self):
        return '{}: {}'.format( self.label, self.expr )
