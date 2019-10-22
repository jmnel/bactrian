from enum import Enum
from .expression import Expression

class Relation(Expression):

    def __init__(self, lhs, rhs):
        from .expression import bractify
        self.args = [ bractify( lhs ), bractify( rhs ) ];

    def lhs(self):
        return self.args[0]

    def rhs(self):
        return self.args[1]

    class RelationType(Enum):
        LessThan = 0,
        GreaterThan = 1,
        StrictLessThan = 2,
        StrictGreaterThan = 3,
        EqualTo = 4,
        NotEqualTo = 5

class LessThan(Relation):
    def __init__(self, lhs, rhs):
        super(LessThan, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.LessThan

    def __repr__(self):
        str = '{} <= {}'.format( self.lhs(), self.rhs() )
        return str

class GreaterThan(Relation):
    def __init__(self, lhs, rhs):
        super(GreaterThan, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.GreaterThan

    def __repr__(self):
        str = '{} >= {}'.format( self.lhs(), self.rhs() )
        return str

class LessThanStrict(Relation):
    def __init__(self, lhs, rhs):
        super(LessThanStrict, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.LessThanStrict

    def __repr__(self):
        str = '{} < {}'.format( self.lhs(), self.rhs() )
        return str

class GreaterThanStrict(Relation):
    def __init__(self, lhs, rhs):
        super(GreaterThan, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.GreaterThanStrict

    def __repr__(self):
        str = '{} > {}'.format( self.lhs(), self.rhs() )
        return str

class EqualTo(Relation):
    def __init__(self, lhs, rhs):
        super(EqualTo, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.EqualTo

    def __repr__(self):
        str = '{} == {}'.format( self.lhs(), self.rhs() )
        return str

class NotEqualTo(Relation):
    def __init__(self, lhs, rhs):
        super(NotEqualTo, self).__init__(lhs,rhs)
        self.relation_type = self.RelationType.NotEqualTo

    def __repr__(self):
        str = '{} != {}'.format( self.lhs(), self.rhs() )
        return str
