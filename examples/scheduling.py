# Scheduling problem from Eiselt pg. 81
from bactrian import Variable, Objective, Constraint, Problem, scipylinprog

# Decision variables
x1 = Variable('x1')   # staff midnight - 4 a.m.
x2 = Variable('x2')   # staff 4 a.m. - 8 a.m.
x3 = Variable('x3')   # staff 8 a.m. - noon
x4 = Variable('x4')   # staff 12 noon - 4 p.m.
x5 = Variable('x5')   # staff 4 p.m. - 8 p.m.
x6 = Variable('x6')   # staff 8 p.m. - midnight

# Objective function: sum of staff on all shifts
total_staff = Objective('total_staff', x1 + x2+ x3 + x4 + x5 + x6)

# Minimum staffing constraints for each duration
c1 = Constraint('c1', x1 + x6 >= 6)
c2 = Constraint('c2', x1 + x2 >= 8)
c3 = Constraint('c3', x2 + x3 >= 11)
c4 = Constraint('c4', x3 + x4 >= 9)
c5 = Constraint('c5', x4 + x5 >= 18)
c6 = Constraint('c6', x5 + x6 >= 11)

# Define problem model.
scheduling = Problem('scheduling', (total_staff,
    [x1, x2, x3, x4, x5, x6], [c1, c2, c3, c4, c5, c6 ]))

# Print model
print(scheduling)

# Solve minimization model.
scipylinprog(scheduling)
