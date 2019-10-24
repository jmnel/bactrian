from .expression import Expression, bractify

class Mul(Expression):
    def __init__(self, args):
        assert len(args) > 1, 'Mul must have atleast 2 args'

        new_args = list()
        for a in args:
            if isinstance(a, Mul):
                new_args.extend(a.args)
            else:
                new_args.append(a)
        self.args = tuple(bractify(e) for e in new_args )

    def __repr__(self):
        from .add import Add
        def to_str_arg(a):
            s = str(a)
            return (('( %s )' % s) if isinstance(a, Add) else s)
        return ' * '.joint(to_str_arg(a) for a in self.args)
