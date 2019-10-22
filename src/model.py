import numpy as np

class Model:
    variables = {}
    constraints = {}
    mat_a = []
    b = []

    def addVariable(self, variable ):
        self.variables[ variable.label ] = variable

    def addConstraint( self, constraint ):
        self.constraints[ constraint.label ] = constraint
        self.mat_a.append( constraint.a_row )
        self.b.append( constraint.b )


    def __repr__(self):
        str = ''
        str += 'Model\n-----\n'
        for i in range( 0, len( self.variables ) ):
            str += '{}: {}\n'.format( i, self.variables[i] )
        return str

ns_model = Model()


