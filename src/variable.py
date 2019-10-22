import sympy as sym
from workbook import ns_workbook

class Variable(sym.Symbol):
    def __init__(self, label):
        super(Variable, self).__init__()

        self.label = label
        self.index = len(ns_workbook.variables)
        ns_workbook.add_variable(self)

    def __repr__(self):
        return '`{}`'.format( self.label )


