# Bactrian

Simplified Python modeling language library to model and solve optimization and operations
research problems, aiming to mirror the API of Dromedary Studio

## Getting Started

### Example

Solve the following linear programming model

<img src="https://latex.codecogs.com/gif.latex?\text{minimize}\:&space;x&space;&plus;&space;2y" title="\text{minimize}\: x + 2y" />

<br>

<img src="https://latex.codecogs.com/gif.latex?\text{s.t.}\quad&space;\begin{matrix}&space;-5x&space;&plus;&space;2y&space;&&space;=&space;&&space;7&space;\\&space;x&space;&plus;&space;y&space;&&space;\geq&space;&&space;26&space;\\&space;x,&space;y&space;&&space;\geq&space;&&space;0&space;\\&space;\end{matrix}" title="\text{s.t.}\quad \begin{matrix} -5x + 2y & = & 7 \\ x + y & \geq & 26 \\ x, y & \geq & 0 \\ \end{matrix}" />

```python
from bactrian import Variable, Constraint, Objective, Problem, scipylinprog

# Define decision variables.
x = Variable('x')
y = Variable('y')

# Define objective function.
obj = Objective('obj', x + 2*y)

# Define constraints.
cstr1 = Constraint('cstr1', -5*x + 2*y == 7)
cstr2 = Constraint('cstr2', x + y >= 26)
# x >= 0 and y >= 0 are implicitly assumed as is standard in LP.

# Define problem.
example_minimize_lp = Problem( 'example_minimize_lp', (obj, [x, y], [cstr1, cstr2]))

# Print model.
print(example_minimize_lp)

# Solve using scipy linprog backend.
scipylinprog(example_minimize_lp)
```

More usage examples can be found under the `examples` directory.

### Prerequisites

This repo is currently private. To install Bactrian with `pip`, you need to have ssh key linked 
to your GitHub account. If you do not have one, 
[follow the guide from GitHub](https://help.github.com/en/enterprise/2.16/user/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### Installing

Install Bactrian with `pip` either globally or in preferrably in a virtual environment.

```bash
$ pip install git+ssh://github.com/jmnel/bactrian.git#egg=bactrian
```

Install Bactrian's dependencies.

```bash
$ pip install mypy numpy scipy typing_expressions 
```

## Development

Either clone the repo directly or preferrably, create a python project. Setup a virtual 
environment (in this example `$ python -m venv env`), and install bactrian with `pip` in editable mode. This will clone the repo into 
`<project-directory>/env/src/` where you can make changes directly,

```bash
$ pip install --editable 'git+ssh://github.com/jmnel/bactrian.git#egg=bactrian'
```

while allowing easy importing of bactrian into your project as follows:

```python
from bactrian import Variable, Constraint, # ... etc.
```

Please refer to [Open Issues](https://github.com/jmnel/bactrian/issues?q=is%3Aissue+is%3Aopen+) for
ideas of where to contribute. Submit pull requests with changes.

## Authors

Jacques Nel [GitHub/jmnel](https://github.com/jmnel) and Askhan Moatamed [GitHub/AskhanM96](https://github.com/AskhanM96)

## License

## Acknowledgements

Bactrian's API is inspired by Dromedary Studio modelling language developed by Dr. Michael Chen
of York University, Toronto.
