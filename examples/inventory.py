from bactrian import Variable
from bactrian import Objective
from bactrian import Constraint
from bactrian import Problem
from bactrian import scipylinprog

# Create decision variables.
x11 = Variable( 'x11' )
x12 = Variable( 'x12' )
x13 = Variable( 'x13' )
x14 = Variable( 'x14' )
x21 = Variable( 'x21' )
x22 = Variable( 'x22' )
x23 = Variable( 'x23' )
x24 = Variable( 'x24' )
x31 = Variable( 'x31' )
x32 = Variable( 'x32' )
x33 = Variable( 'x33' )
x34 = Variable( 'x34' )
x41 = Variable( 'x41' )
x42 = Variable( 'x42' )
x43 = Variable( 'x43' )
x44 = Variable( 'x44' )

# Define objective function.
remaining_stock = Objective( 'cost',
          1.0 * x11 + 1.3 * x12 + 1.7 * x14
        + 1.1 * x22 + 1.3 * x23 + 1.5 * x24
        + 1.2 * x33 + 1.4 * x34 + 1.2 * x44 )

# Define production constraints.
p1 = Constraint( 'p1', x11 + x12 + x13 + x14 <= 100 )
p2 = Constraint( 'p2', x22 + x23 + x24       <= 100 )
p3 = Constraint( 'p3', x33 + x34             <= 160 )
p4 = Constraint( 'p4', x44                   <= 150 )

# Define demand constraints.
d1 = Constraint( 'd1', x11                   >= 50 )
d2 = Constraint( 'd2', x12 + x22             >= 120 )
d3 = Constraint( 'd3', x13 + x23 + x33       >= 150 )
d4 = Constraint( 'd4', x14 + x24 + x34 + x44 >= 160 )

# Define problem.
inventory = Problem( 'inventory', ( remaining_stock,
    [   x11, x12, x13, x14, x21, x22, x23, x24,
        x31, x32, x33, x34, x41, x42, x43, x44 ],
    [   p1, p2, p3, p4, d1, d2, d3, d4 ] ) )

print( inventory )

scipylinprog( inventory )
