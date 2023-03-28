# Lab 03. Two-Phase Simplex

The goal of this is lab is to implement a simplex solver that handle all linear problems. To achieve that, one has to:

* fill missing code in the `saport.simplex.solver.Solver` class
* create two models to test the algorithm, filling missing code in the `example_04_solvable_artificial_vars.py` and `example_05_unfeasible.py` files

## SAPORT

SAPORT = Student's Attempt to Produce an Operation Research Toolkit

Refer to the `example.py` for a quick overview of the API.

The project depends on the fairly recent numpy distribution and Python interpreter (version >= `3.9` is recommended). All depedendencies are listed in `requirements.txt`. One can install them with simple `pip install -r requirements.txt`, but using a virtual environment (e.g. virtualenv) is encouraged ([official tutorial](https://docs.python.org/3/tutorial/venv.html)). 

## How To Run Local Tests

### Solver Class

Just ran the `pytest` command, given you have installed all the requirements from the `requirements.txt`.

In case you were using some weird OS (e.g. Windows), you may have to run `python -m pytest`

### Examples 

The example files are very basic acceptance tests and **are not** used in the grading process.  
*Warning*: to run the examples, you should first implement the simplex algorithm. Otherwise the examples will just hang due to the `pass` methods in the `saport.simplex.solver.Solver`.

Then you can just run every example using `python path_to_example.py`, or you can ran all the examples with: `python test.py`.

## GitLab Setup 

* [ ] Make sure, you have a **private** group 
  * [how to create a group](https://docs.gitlab.com/ee/user/group/#create-a-group)
* [ ] Add @bobot-is-a-bot as the new group member (role: **maintainer**)
  * [how to add a group member](https://docs.gitlab.com/ee/user/group/#add-users-to-a-group)
* [ ] Fork this project into your new **private** group
  * [how to create a fork](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork)

## How To Submit Solutions

* [ ] Clone repository: git clone:
    ```bash 
    git clone <repository url>
    ```
* [ ] Solve the exercises 
    * remember to change only files with `#TODO` comments
* [ ] Commit your changes
    ```bash
    git add <path to the changed files>
    git commit -m <commit message>
    ```
* [ ] Push changes to the gitlab master branch
    ```bash
    git push -u origin master
    ```

The rest will be taken care of automatically. You can check the `GRADE.md` file for your grade / test results. Be aware that it may take some time (up to one hour) till this file appears / gets updated.  

## Repository Guide

```bash
.
├── README.md        # this README
├── conftest.py      # this file enables to call `pytest` without hustle
├── example.py       # just an example, how to create models in SAPORT
├── example_01_solvable.py  # an example of a naive acceptance test for our solver
├── example_02_solvable.py  # same as ^
├── example_03_unbounded.py # same as ^
├── example_04_solvable_artificial_vars.py  # TODO: fill this example based on the example_02...
├── example_05_infeasible.py # TODO: fill this example based on the example_03...
├── requirements.txt # package requirements - install with `pip -r requirements.txt`
├── saport           # directory with the SAPORT source-code   
│   └── simplex      # directory containing code related to the simplex algorithm 
│       ├── expressions        # directory with classes related to the linear programming model components 
│       │   ├── atom.py        # atom is just a single variable with a coefficient
│       │   ├── constraint.py  # class representing linear constraint
│       │   ├── expression.py  # class representing linear expression
│       │   └── objective.py   # class representing objective
│       ├── exceptions.py # project specific exceptions
│       ├── model.py      # class allowing to create linear programming models
│       ├── solution.py   # class representing solutions to the problems
│       ├── solver.py     # this class contains main simplex solver loop
│       └── tableau.py   # TODO: class representing so called simplex tableau — you have to fill some code here!
└── tests                 # directory with local tests
```
