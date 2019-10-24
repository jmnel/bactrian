from enum import Enum
from .expression import Expression, bractify

class Relation(Expression):
    def __init__(self, lhs: Expression, rhs: Expression):
        self.args = [bractify(lhs), bractify(rhs)];

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
    def __init__(self, lhs: Expression, rhs: Expression):
        super(LessThan, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.LessThan

    def __repr__(self):
        return ('%s <= %s' % (str(self.lhs()), str(self.rhs())))

class GreaterThan(Relation):
    def __init__(self, lhs: Expression, rhs: Expression):
        super(GreaterThan, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.GreaterThan

    def __repr__(self):
        return ('%s >= %s' % (str(self.lhs()), str(self.rhs())))

class LessThanStrict(Relation):
    def __init__(self, lhs: Expression, rhs: Expression):
        super(LessThanStrict, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.LessThanStrict

    def __repr__(self):
        return ('%s < %s' % (str(self.lhs()), str(self.rhs())))

class GreaterThanStrict(Relation):
    def __init__(self, lhs: Expression, rhs: Expression):
        super(GreaterThan, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.GreaterThanStrict

    def __repr__(self):
        return ('%s > %s' % (str(self.lhs()), str(self.rhs())))

class EqualTo(Relation):
    def __init__(self, lhs: Expression, rhs: Expression):
        super(EqualTo, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.EqualTo

    def __repr__(self):
        return ('%s == %s' % (str(self.lhs()), str(self.rhs())))

class NotEqualTo(Relation):
    def __init__(self, lhs: Expression, rhs: Expression):
        super(NotEqualTo, self).__init__(lhs, rhs)
        self.relation_type = self.RelationType.NotEqualTo

    def __repr__(self):
        return ('%s != %s' % (str(self.lhs()), str(self.rhs())))
