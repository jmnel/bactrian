# Diet problem from Eiselt pg. 67

from bactrian import Variable, Objective, Constraint, Problem, scipylinprog

x1 = Variable( 'x1' )
x2 = Variable( 'x2' )
x3 = Variable( 'x3' )
x4 = Variable( 'x4' )
x5 = Variable( 'x5' )
x6 = Variable( 'x6' )

cost = Objective( 'cost', 3.29*x1 + 3.99 * x2 + 0.45*x3 + 0.48*x4 + 0.4*x5 + 0.25*x6 )

c1 = Constraint('c1', 24*x1 + 8*x2 + 3*x3 + 5*x4 + 8.5*x5 + 2*x6 >= 56 )
c2 = Constraint('c2', 3*x1 + 3*x2 + 3*x3 + 3*x4 + x6 >= 30 )
c3 = Constraint('c3', 44*x1 + 96*x2 + 5*x3 + 27*x4 + 13*x5 + 27*x6 >= 130 )
c4 = Constraint( 'c4', 530*x1 + 510*x2 + 25*x3 + 140*x4 + 130*x5 + 110*x6 >= 1800 )
c5 = Constraint( 'c5', 530*x1 + 510*x2 + 25*x3 + 140*x4 + 130*x5 + 110*x6 <= 2200 )
c6 = Constraint( 'c6', 65*x1 + 30*x2 + 20*x5 <= 300 )
c7 = Constraint( 'c7', 10*x1 + 3*x2 + 27*x3 + 10*x5 + 2*x6 >= 100 )
c8 = Constraint( 'c8', 4*x1 + 33*x2 + 137*x3 + 4*x5 + 100*x6 >= 100 )
c9 = Constraint( 'c9', 10*x1 + 8*x2 + 3*x5 <= 24 )
c10 = Constraint( 'c10', 1020*x1 + 180*x2 + 24*x3 + 270*x4 + 125*x5 <= 2400 )

diet = Problem( 'diet', ( cost, [x1, x2, x3, x4, x5, x6], [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 ] ) )

print( diet )

scipylinprog( diet )
