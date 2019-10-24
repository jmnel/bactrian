from scipy.optimize import linprog
from .problem import Problem

def scipylinprog(problem: Problem, solver_method: str = 'revised simplex'):

    valid_methods = {'interior-point', 'revised simplex', 'simplex'}
    if not solver_method in valid_methods:
        raise ValueError( '%s is invalid solver method\n'\
        'valid methods are: %s' % (solver_method, repr(valid_methods)
            [1:-1]))

    has_inequality_constraints = len(problem.mat_a_ub) != 0
    has_equality_constraints = len(problem.mat_a_eq) != 0

    # Case 1: Problem has both inequality and equality constraints.
    if has_inequality_constraints and has_equality_constraints:
        res = linprog(problem.c, A_ub=problem.mat_a_ub, b_ub=problem.b_ub,
            A_eq=problem.mat_a_eq, b_eq=problem.b_eq, method=solver_method)

    # Case 2: Problem has only inequality constraints.
    elif has_inequality_constraints and (not has_equality_constraints):
        res = linprog(problem.c, A_ub=problem.mat_a_ub, b_ub=problem.b_ub,
            method=solver_method)

    # Case 3: Problem has only equality constraints.
    elif (not has_inequality_constraints) and has_equality_constraints:
        res = linprog(problem.c, A_eq=problem.mat_a_eq, b_eq=problem.b_eq,
            method=solver_method)

    # Case 4: Problem has no constraints.
    else :
        raise ValueError( 'No constraints provided' )

    print( '# Solution Report' )
    if res.success:
        print('# Solverstatus: Optimization terminated successfully')
        print('# Objective value: %f' % res.fun)
        print('# Primal values:')
        for i, var in enumerate(problem.variables):
            print('%s= %f' % problem.variables[i].label, res.x[i])
