from bactrian import Variable
from bactrian import Objective
from bactrian import Constraint
from bactrian import Problem
from bactrian import scipylinprog

e3 = Variable('e3')
w1 = Variable('w1')
w2 = Variable('w2')
w3 = Variable('w3')
w4 = Variable('w4')

efficiency_3 = Objective('efficiency_3', e3)
c1 = Constraint('c1', 65*w1 + 83*w2 + 61*w3 + 81*w4 >= 61)
c2 = Constraint('c2', 123*w1 + 135*w2 + 92*w3 + 110*w4 >= 92)
c3 = Constraint('c3', 25*w1 + 33*w2 + 28*w3 + 29*w4
        - 28*e3 <= 0)
c4 = Constraint('c4', 2*w1 + 3*w2 + 2*w3 + 2*w4
        - 2*e3 <= 0)
c5 = Constraint('c5', 1300*w1 + 1800*w2 + 1300*w3 + 1200*w4
        - 1300*e3 <= 0)

dea = Problem('dea', (efficiency_3, [e3, w1, w2, w3, w4],
    [c1, c2, c3, c4, c5]))

print(dea)

scipylinprog(dea)
