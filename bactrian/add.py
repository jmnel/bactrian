from .expression import Expression, bractify

class Add(Expression):

    def __init__(self, *args):
        assert len(args) > 1, 'Add must have atleast 2 args.'

        new_args = list()
        for a in args:
            if isinstance(a, Add):
                new_args.extend(a.args)
            else:
                new_args.append(a)

        self.args = tuple( bractify(e) for e in new_args )

    def __repr__(self):
        return " + ".join(str(a) for a in self.args)


#from .numeric_types import Float
