import datetime

class Workbook:

    variables = {}
    constraints = {}
    objectives = {}
    problems = {}

    output_str = ''

    def __init__(self):
        print( 'Dromedary 1.0.0 (August 22 2019 9:39:22) [Python 3.7.3] :: Dromedary Inc.' )

    def add_variable(self, variable):
        self.variables[ variable.label ] = variable

    def add_constraint(self, constraint):
        self.constraints[ constraint.label ] = constraint

    def add_object(self, objectives):
        self.objectives[ objective.label ] = objective

    def add_problem(self, problem):
        self.problems[ problem.label ] = problem

    def print_output( str ):
        self.output_str+=str;
        self.output_str+='\n'

    def save_output( path ):
        f = open( path, 'w+' )
        f.write( self.output_str )
        f.close()

ns_workbook = Workbook()

