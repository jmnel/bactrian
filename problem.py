import numpy as np
from workbook import ns_workbook

class Problem:

    def __init__(self, label, params):
        self.label = label
        self.objective = params[0]
        self.variables = params[1]
        self.constraints = params[2]

        ns_workbook.add_problem(self)

        self.c = self.objective.c

        self.m = len( self.constraints )
        self.n = len( self.variables )
        self.mat_a = np.zeros( (self.m, self.n) )
        self.b = np.zeros( self.m )
        for i in range( 0, self.m ):
            self.mat_a[i] = self.constraints[i].a_row
            self.b[i] = self.constraints[i].b

    def __repr__(self):
        str = '# Problem: {}\n'.format(self.label)
        str = 'List of variables:\n'
        str+= '{}'.format(self.variables[0])
        for i in range(1,len(self.variables)):
            str+= ', {}'.format( self.variables[i] )
        str+='\n'
        str+='# Objective:\n'
        str+='minimize {}: {}\n'.format( self.objective.label, self.objective.expr )
        str+='# List of constraints:\n'
        for c in self.constraints:
            str+='{}: {}\n'.format( c.label, c.expr )
        str+='# Call fullreport(name) to get more details of the variable, obj, or constraint of the name.'
        str+='\n\n\n'

        return str


