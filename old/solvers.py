from scipy.optimize import linprog

def scipylinprog( problem ):
    res = linprog( problem.c, A_ub=problem.mat_a, b_ub = problem.b,
            bounds=(0,None), method='revised simplex')

    print('# Solution Report')
    if res.success:
        print('# Solverstatus: Optimization terminated successfully')
        print('# Objective value: {}'.format( res.fun ) )
        print('# Primal values:')
        for i in range(0, len(problem.variables)):
            print('{}= {}'.format( problem.variables[i].label, res.x[i] ) )





