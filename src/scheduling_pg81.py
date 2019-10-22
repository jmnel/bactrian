from variable import Variable
from constraint import Constraint
from objective import Objective
from problem import Problem
from solvers import scipylinprog

x1 = Variable( 'x1' )
x2 = Variable( 'x2' )
x3 = Variable( 'x3' )
x4 = Variable( 'x4' )
x5 = Variable( 'x5' )
x6 = Variable( 'x6' )

cost = Objective( 'cost', 1 * x1 + 1 * x2+ 1 * x3 + 1 * x4 + 1 * x5 + 1 * x6 )
c1 = Constraint( 'c1', 1 * x1 + 1 * x6 >= 6 )
c2 = Constraint( 'c2', 1 * x1 + 1 * x2 >= 8 )
c3 = Constraint( 'c3', 1 * x2 + 1 * x3 >= 11 )
c4 = Constraint( 'c4', 1 * x3 + 1 * x4 >= 9 )
c5 = Constraint( 'c5', 1 * x4 + 1 * x5 >= 18 )
c6 = Constraint( 'c6', 1 * x5 + 1 * x6 >= 11 )

scheduling = Problem( 'scheduling', ( cost, [x1, x2, x3, x4, x5, x6], [c1, c2, c3, c4, c5, c6 ] ) )

print( scheduling )

scipylinprog( scheduling )
