from __future__ import annotations
from typing import List
from numpy.typing import ArrayLike
import numpy as np
import math
from . import model as ssmod

eps = 0.000000001

class Tableau:
    """
        A class to represent a tableau to linear programming problem.

        Attributes
        ----------
        model : Model
            model corresponding to the tableau
        table : numpy.Array
            2d-array with the tableau

        Methods
        -------
        __init__(model: Model, table: array) -> Tableau:
            constructs a new tableau for the specified model and initial table
        objective_coefficients() -> numpy.Array:
            returns a vector containing factors in the cost row
        objective() -> float:
            returns the objective value of solution represented in tableau
        is_optimal() -> bool:
            checks whether the current solution is optimal
        choose_entering_variable() -> int:
            finds index of the variable, that should enter the basis next
        is_unbounded(col: int) -> bool:
            checks whether the problem is unbounded
        choose_leaving_variable(col: int) -> int:
            finds index of the variable, that should leave the basis next
        pivot(col: int, row: int):
            updates tableau using pivot operation with given entering and leaving variables
        extract_assignment() -> List[float]:
            returns assignment corresponding to the tableau
        extract_basis() -> List[int]
            returns list of indexes corresponding to the variables belonging to the basis
    """
    model: ssmod.Model
    table: ArrayLike

    def __init__(self, model: ssmod.Model, table: ArrayLike):
        self.model = model
        self.table = table

    def objective_coefficients(self) -> ArrayLike:
        return self.table[0,:-1] 

    def objective(self) -> float:
        return self.table[0, -1]

    def is_optimal(self) -> bool:
        return self.objective_coefficients().min() >= -eps

    def choose_entering_variable(self) -> int:
        return self.objective_coefficients().argmin()

    def is_unbounded(self, col: int) -> bool:
        return self.table[1:, col].max() <= eps 

    def choose_leaving_variable(self, col: int) -> int:
        # List comprehensions magic:
        # - let's iteratate over the column - `for i,c in enumerate(self.table[:, col])`
        # - let's consider only positive values: `if c > eps` and ignore the first row as it is objective: `i > 0`
        # - as the result, let's return a tuple, where:
        #   * first element is bound divided by the given coefficien: self.table[i,-1] / c
        #   * second element is index of the row corresponding to the result
        # Effectively, the `indicators` list contains division results and their corresponding row indices
        indicators = [(self.table[i,-1] / c, i) for i,c in enumerate(self.table[:, col]) if c > eps and i > 0]
        
        # Let't return the minimal element from the list, the correspnding index of the row, to be exact 
        # - in python when two tuples are compared, e.g. (1,3) and (0, 5) — the comparison is lexicographical:
        #   we compare elements starting from left, therefore (0, 5) is smaller than (1, 3), as 0 is smaller than 1
        # - we take care of the scenario when there is no row constraining the variable 
        #   `a if b else c` is the same as `c ? a : b` in C/C++
        return min(indicators)[1] if len(indicators) > 0 else None

    def pivot(self, row: int, col: int):
        # First, we normalize to row to have `1` at the pivot coords
        self.table[row] /= self.table[row,col]

        # Then we iterate over all the rows in the table
        for i,r in enumerate(self.table):
            # we ignore the pivot row
            if i == row:
                continue
            # we substract pivot row from the row r[col] times
            r -= r[col] * self.table[row]

    def extract_assignment(self) -> List[float]:
        rows_n, cols_n = self.table.shape
        assignment = [0.0 for _ in range(cols_n - 1)]
        basis = self.extract_basis()
        for r in range(1, rows_n):
            var_index = basis[r - 1]
            assignment[var_index] = self.table[r, -1]
        
        return assignment
    
    def extract_basis(self) -> List[int]:
        rows_n, cols_n = self.table.shape
        basis = [-1 for _ in range(rows_n -1)]
        for c in range(cols_n - 1):
            column = self.table[:,c]
            belongs_to_basis = math.isclose(column.min(), 0.0, eps) \
                           and math.isclose(column.max(), 1.0, eps) \
                           and math.isclose(column.sum(), 1.0, eps)
            if belongs_to_basis:
                row = np.where(column == 1.0)[0][0]
                # [row-1] because we ignore the cost variable in the basis
                basis[row-1] = c
        return basis

    def __str__(self) -> str:
        def cell(x: float, w: int) -> str:
            return '{0: >{1}}'.format(x, w)

        cost_name = self.model.objective.name()
        basis = self.extract_basis()
        header = ["basis", cost_name] + [var.name for var in self.model.variables] + ["b"]
        longest_col = max([len(h) for h in header])

        rows = [[cost_name]] + [[self.model.variables[i].name] for i in basis]

        for (i,r) in enumerate(rows):
            cost_factor = 0.0 if i > 0 else 1.0
            r += ["{:.3f}".format(v) for v in [cost_factor] + list(self.table[i])]
            longest_col = max(longest_col, max([len(v) for v in r]))

        header = [cell(h, longest_col) for h in header]
        rows = [[cell(v, longest_col) for v in row] for row in rows]

        cell_sep = " | "

        result = cell_sep.join(header) + "\n"
        for row in rows:
            result += cell_sep.join(row) + "\n"
        return result