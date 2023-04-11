import logging
from saport.simplex.model import Model 

from saport.simplex.model import Model

def create_model() -> Model:
    model = Model("example_05_infeasible")
    # TODO:
    # fill missing test based on the example_03_unbounded.py
    # to make the test a bit more interesting:
    # * make sure model is infeasible
    x1 = model.create_variable("x1")
    x2 = model.create_variable("x2")

    model.add_constraint(2*x1 >= 1200)
    model.add_constraint(x1 + x2 <= 400)
    model.add_constraint(2*x1+(3/2)*x2 >= 900)

    model.maximize(-2*x1 - 3*x2)
    return model

def run():
    model = create_model()
    # TODO:
    # add a test "assert something" based on the example_03_unbounded.py
    # TIP: you may use other solvers (e.g. https://online-optimizer.appspot.com)
    #      to find the correct solution
    solution = model.solve()

    if solution.is_bounded:
        raise AssertionError("Your algorithm found a solution to an unbounded problem. This shouldn't happen...")
    else:
        logging.info("Congratulations! This problem is unbounded and your algorithm has found that :)")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    run()
