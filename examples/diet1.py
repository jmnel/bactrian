from bactrian import Variable
from bactrian import Objective
from bactrian import Constraint
from bactrian import Problem
from bactrian import scipylinprog

x1 = Variable( 'x1' )
x2 = Variable( 'x2' )

cost = Objective( 'cost', 10 * x1 + 7 * x2 )

c1 = Constraint( 'c1', 20 * x1 + 20 * x2 >= 60 )
c2 = Constraint( 'c2', 15 * x1 + 3 * x2 >= 15 )
c3 = Constraint( 'c3', 5 * x1 + 10 * x2 >= 20 )

diet = Problem( 'diet', ( cost, [x1, x2], [c1, c2, c3] ) )

print( diet )

scipylinprog( diet )
