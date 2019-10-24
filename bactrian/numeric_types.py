from .expression import Expression

class Numeric:
    pass

class Float(Numeric, Expression):
    def __init__(self, value: float):
        self.value = value

    def __float__(self):
        return self.value

    def __repr__(self):
        return ('%f' % self.value)

    def __neg__(self):
        return Float(-self.vaue)

class Integer(Numeric, Expression):
    def __init__(self, value: int):
        self.value = value

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return ('%d' % self.value)

    def __neg__(self):
        return Integer(-self.value)
