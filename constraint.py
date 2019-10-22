from enum import Enum
import sympy as sym
import numpy as np
from helpers import *
from workbook import ns_workbook

class Constraint:
    class RelationType(Enum):
        LessThan = 1,
        Equality =2 ,
        GreaterThan = 3

    def __init__(self, label, expr):
        self.label = label
        self.expr = expr

        if type(expr) is sym.LessThan:
            self.relation_type = self.RelationType.LessThan
        elif type(expr) is sym.Equality:
            #@todo: Not implemented correctly yet
            assert(False)
            self.relation_type = self.RelationType.Equality
        elif type(expr) is sym.GreaterThan:
            self.relation_type = self.RelationType.GreaterThan
        else:
            raise Exception( 'constraint expression is not a valid relation' )

        if not is_scalar( expr.args[1] ):
            raise Exception( 'rhs of constraint expression must be constant scalar' )

        rhs = expr.args[1]

        self.a_row = np.zeros( len( ns_workbook.variables ) )
        lhs = expr.args[0]

        lhs_terms = parse_linear_combination( lhs )

        for term in lhs_terms:
            coef = term[0]
            coef_index = term[1].index

            if self.relation_type == self.RelationType.GreaterThan:
                coef = -coef

            self.a_row[ coef_index ] =+ coef

        if self.relation_type == self.RelationType.GreaterThan:
                rhs = -rhs
        self.b = rhs

        ns_workbook.add_constraint( self )
