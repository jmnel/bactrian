import numpy as np
from typing_extensions import Final

class Problem:
    def __init__(self, label, params):
        self.label = label
        self.objective = params[0]
        self.variables = params[1]
        self.constraints = params[2]

        self.M : Final = len( self.constraints )
        self.N : Final = len( self.variables )

        self._assign_variable_indices()
        self._build_objective_vector()
        self._build_constraints_matrix()

    def _assign_variable_indices(self):
        for i in range( 0, len( self.variables ) ):
            self.variables[i].index = i

    def _build_objective_vector(self):
        from .expression import parse_linear_combination
        terms = parse_linear_combination( self.objective.expr )
        self.c = np.zeros( self.N )
        for t in terms:
            coef = t[0]
            coef_index = t[1].index
            self.c[ coef_index ] = coef

    def _build_constraints_matrix(self):
        from .expression import parse_linear_combination
        from .relation import Relation
        self.b_ub = []
        self.b_eq = []
        self.mat_a_ub = []
        self.mat_a_eq = []

        for constraint in self.constraints:
            constraint_type = constraint.expr.relation_type

            lhs = constraint.expr.lhs()
            rhs = constraint.expr.rhs()

            b = rhs
            a_row = np.zeros( self.N )

            lhs_terms = parse_linear_combination( lhs )
            for t in lhs_terms:
                coef = t[0]
                coef_index = t[1].index
                a_row[ coef_index ] = coef

            if constraint_type == Relation.RelationType.LessThan:
                self.mat_a_ub.append( a_row )
                self.b_ub.append( b )
            elif constraint_type == Relation.RelationType.GreaterThan:
                a_row = [ -e for e in a_row ]
                b = -b
                self.mat_a_ub.append( a_row )
                self.b_ub.append( b )
            elif constraint_type == Relation.RelationType.EqualTo:
                self.mat_a_eq.append( a_row )
                self.b_eq.append( b )
            else:
                raise Exception( 'Invalid relation type' )


