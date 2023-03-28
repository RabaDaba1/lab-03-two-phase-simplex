import logging
from saport.simplex.model import Model 

from saport.simplex.model import Model

def create_model() -> Model:
    model = Model("example_05_infeasible")
    # TODO:
    # fill missing test based on the example_03_unbounded.py
    # to make the test a bit more interesting:
    # * make sure model is infeasible
    return model

def run():
    model = create_model()
    # TODO:
    # add a test "assert something" based on the example_03_unbounded.py
    # TIP: you may use other solvers (e.g. https://online-optimizer.appspot.com)
    #      to find the correct solution
    logging.info("This test is empty but it shouldn't be, fix it!")
    raise AssertionError("Test is empty")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    run()
