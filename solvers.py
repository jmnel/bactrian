from scipy.optimize import linprog

def scipylinprog( problem ):

    solver_method = 'revised simplex'

    has_inequality_constraints = len( problem.mat_a_ub ) > 0
    has_equality_constraints = len( problem.mat_a_eq ) > 0

    # Case 1: Problem has both inequality and equality constraints.
    if has_inequality_constraints and has_equality_constraints:
        res = linprog( problem.c, A_ub = problem.mat_a_ub, b_ub = problem.b_ub,
            A_eq = problem.mat_a_eq, b_eq = problem.b_eq, method='revised simplex')

    # Case 2: Problem has only inequality constraints.
    elif has_inequality_constraints and not has_equality_constraints:
        res = linprog( problem.c, A_ub = problem.mat_a_ub, b_ub = problem.b_ub,
            method='revised simplex')

    # Case 3: Problem has only equality constraints.
    elif not has_inequality_constraints and has_equality_constraints:
        res = linprog( problem.c, A_eq = problem.mat_a_eq, b_eq = problem.b_eq,
            method='revised simplex')

    # Case 4: Problem has no constraints.
    else :
        raise Exception( 'No constraints provided' )

    print( '# Solution Report' )
    if res.success:
        print( '# Solverstatus: Optimization terminated successfully' )
        print( '# Objective value: {}'.format( res.fun ) )
        print( '# Primal values:')
        for i in range(0, len( problem.variables ) ):
            print( '{}= {}'.format( problem.variables[i].label, res.x[i] ) )

