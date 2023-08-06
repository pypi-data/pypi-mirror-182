"""Cryptarithmetic puzzle.

First attempt to solve equation CP + IS + FUN = TRUE
where each letter represents a unique digit.

This problem has 72 different solutions in base 10.
"""
from ortools.constraint_solver import pywrapcp


def main():
    # Constraint programming engine
    solver = pywrapcp.Solver('SEND MORE MONEY')

    base = 10

    # Decision variables.
    digits = list(range(0, base))
    digits_without_zero = list(range(1, base))
    y = solver.IntVar(digits_without_zero, 'Y')
    o = solver.IntVar(digits, 'O')
    u = solver.IntVar(digits, 'U')
    r = solver.IntVar(digits, 'R')
    h = solver.IntVar(digits_without_zero, 'H')
    e = solver.IntVar(digits, 'E')
    a = solver.IntVar(digits, 'A')
    t = solver.IntVar(digits, 'T')

    # We need to group variables in a list to use the constraint AllDifferent.
    letters = [y,o,u,r,h,e,a,t]

    # Verify that we have enough digits.
    assert base >= len(letters)

    # Define constraints.
    solver.Add(solver.AllDifferent(letters))

    # CP + IS + FUN = TRUE
    solver.Add(r + u + base * (u+o) + base * base * (y+o) + base * base * base * (y) == t +
               base * r + base * base * a + base * base * base * e + base*base*base*base*h)

    solution_count = 0
    db = solver.Phase(letters, solver.INT_VAR_DEFAULT, solver.INT_VALUE_DEFAULT)
    solver.NewSearch(db)
    while solver.NextSolution():
        print(letters)
        
        solution_count += 1
    solver.EndSearch()
    print(f'Number of solutions found: {solution_count}')


if __name__ == '__main__':
    main()
