# Bactrian

Simplified Python modeling language library to model and solve optimization and operations
research problems, aiming to mirror the API of Dromedary Studio

## Getting Started

### Example

Solve the following linear programming model

<img src="http://www.sciweavers.org/tex2img.php?eq=x%2B2y%5Crightarrow%5Cmin%0A%5C%5C%5C%5C%0A%5Ctext%7Bsubject%20to%3A%7D%5Cquad%0A%5Cbegin%7Bmatrix%7D%0A-5x%2B2y%20%26%20%3D%20%26%207%20%5C%5C%0Ax%2B%20y%20%26%20%5Cgeq%20%26%2026%20%5C%5C%0Ax%20%5Cgeq%200%2C%20y%20%5Cgeq%200%20%5C%5C%0A%5Cend%7Bmatrix%7D&bc=White&fc=Black&im=gif&fs=12&ff=modern&edit=0" align="center" border="0" alt="x+2y\rightarrow\min\\\\\text{subject to:}\quad\begin{matrix}-5x+2y & = & 7 \\x+ y & \geq & 26 \\x \geq 0, y \geq 0 \\\end{matrix}" width="236" height="101" />

```python
from bactrian import Variable, Constraint, Objective, Problem, scipylinprog

# Define decision variables.
x = Variable('x')
y = Variable('y')

# Define objective function.
obj = Objective('obj', x + 2y)

# Define constraints.
cstr1 = Constraint('cstr1', -5x + 2y == 7)
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
