import numpy as np
from typing_extensions import Final

class Problem:
    def __init__(self, label: str, params: tuple):
        from .label import label
        self.label = validate_label(label)
        self.objective, self.variables, self.constraints = params

        # Do you think this is a good place to make use of typing 
        # extensions?
        self.M: Final = len(self.constraints)
        self.N: Final = len(self.variables)

        self._assign_variable_indices()
        self._build_objective_vector()
        self._build_constraints_matrix()

        print( 'Dromedary 1.0.0 (August 22 2019 9:39:22) [Python 3.7.3] :: Dromedary Inc.' )

    def _assign_variable_indices(self):
        for i, var in enumerate(self.variables):
            var.index = i

    def _build_objective_vector(self):
        from .expression import parse_linear_combination
        terms = parse_linear_combination(self.objective.expr)
        self.c = np.zeros(self.N)
        for t in terms:
            coef, coef_index = t[0], t[1].index
            self.c[coef_index] = coef

    def _build_constraints_matrix(self):
        from .expression import parse_linear_combination
        from .relation import Relation

        self.b_ub = list()
        self.b_eq = list()
        self.mat_a_ub = list()
        self.mat_a_eq = list()

        for constraint in self.constraints:
            constraint_type = constraint.expr.relation_type
            lhs = constraint.expr.lhs()
            rhs = constraint.expr.rhs()

            lhs_terms = parse_linear_combination( lhs )
            b = rhs
            a_row = np.zeros( self.N )

            for t in lhs_terms:
                coef, coef_index = t[0], t[1].index
                a_row[coef_index] = coef

            if constraint_type == Relation.RelationType.LessThan:
                self.mat_a_ub.append(a_row)
                self.b_ub.append(b)
            elif constraint_type == Relation.RelationType.GreaterThan:
                a_row = [-e for e in a_row]
                b = -b
                self.mat_a_ub.append(a_row)
                self.b_ub.append(b)
            elif constraint_type == Relation.RelationType.EqualTo:
                self.mat_a_eq.append(a_row)
                self.b_eq.append(b)
            else:
                raise TypeError( 'Unsupported relation type' )

    def __repr__(self):
        return (\
"""# Problem: %s
# List of variables:
%s
# Objective:
%s  %s
# List of constraints:
%s
# Call fullreport(name) to get more details of the variables, obj, or
constraint of the name.
\n\n
""" % (self.label, ', '.join(str(var) for var in self.variables),
    self.objective.direction, str(self.objective),
    '\n'.join(str(ctrn) for cstr in self.constraints)))
