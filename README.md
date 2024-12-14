# Python Type Error Example

This repository demonstrates a common Python error: a `TypeError` that occurs when performing arithmetic operations on a list containing elements of mixed data types (e.g., integers and strings).

The `bug.py` file contains the erroneous code.  The `bugSolution.py` file shows how to correct this error using type checking or exception handling.

The error occurs because Python's `sum()` function expects all elements to be numbers.  Mixing data types leads to an unexpected `TypeError`.

Solutions include either checking the list's type beforehand or using a `try-except` block to handle potential errors more gracefully.  See `bugSolution.py` for examples of both methods.