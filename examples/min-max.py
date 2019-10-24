from bactrian import Variable
from bactrian import Objective
from bactrian import Constraint
from bactrian import Problem
from bactrian import scipylinprog

x = Variable('x')
e = Variable('e')

obj = Objective('obj', e)

c11 = Constraint('c1', 2 * x - e <= 1)
c12 = Constraint('c2', 2 * x + e >= 1)
c21 = Constraint('c1', x - e <= 1)
c22 = Constraint('c2', x + e >= 1)

min_max = Problem('min_max', (obj, [x, e], [c11, c12, c21, c22]))

print(min_max)

scipylinprog(min_max)
