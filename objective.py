import sympy as sym
import numpy as np
from workbook import ns_workbook
from variable import Variable

class Objective:
    def __init__(self, label, expr):
        self.label = label
        self.expr = expr
        self.c = np.zeros( len( ns_workbook.variables ) )
        assert( len( expr.args ) <= len( self.c ) )
        assert( type(expr) is sym.Add )
        for i in range(0, len( expr.args ) ):
            assert( type( expr.args[i] ) is sym.Mul or
                    type(expr.args[i] ) is Variable )

            if( type(expr.args[i] ) is Variable ):
                v = expr.args[i]
                coef_index = ns_workbook.variables[ v.label ].index
                self.c[ coef_index ] = 1.0
            else:
                assert( len( expr.args[i].args ) == 2 )

                coef_index = 0
                coef = 0.0

                if callable( getattr(expr.args[i].args[0], "__float__", False) ) :
                    assert( type( expr.args[i].args[1] ) is Variable )
                    coef =  expr.args[i].args[0]
                    v = expr.args[i].args[1]
                    coef_index = ns_workbook.variables[v.label].index
                elif type( expr.args[i].args[0] ) is Variable :
                    assert( callable( getattr( expr.args[i].args[1], "__float__", False ) ) )
                    coef = expr.args[i].args[1]
                    v = expr.args[i].args[0]
                    coef_index = ns_workbook.variables[v.label].index
                else:
                    assert(False)

                self.c[ coef_index ] = coef

