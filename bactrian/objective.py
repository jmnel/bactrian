from .expression import Expression

class Objective:
    def __init__(self, label: str, expr: Expression, direction: str='minimize'):
        from .label import validate_label
        valid_dirs = {'minimize', 'maximize'}
        if not direction in valid_dirs:
            raise ValueError( '%s is not a valid direction\n
            valid directions are: %s' % (direction, repr(valid_dirs)[1:-1]))
        self.label = validate_label(label)

        # I see you suggestion to negate expression here for maximize,
        # but this affects printing of objective function. I think it is
        # better to handle that in the solver.
        self.expr = expr

    def __repr__(self):
        return ('%s: %s' % (self.label, str(self.expr)))
