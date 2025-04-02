# cot-4500-as3b

# COT 4500 - Assignment 3B

## Description

This project contains solutions to Assignment 3B for COT 4500. It demonstrates the implementation of core numerical methods using **pure Python (no external libraries like NumPy)**, ensuring compatibility with IDLE 3.13.

The assignment covers:

1. **Gaussian Elimination** with Backward Substitution
2. **LU Factorization** and Determinant Calculation
3. **Diagonal Dominance Check**
4. **Positive Definiteness Check**

---

## Folder Structure

## How to Run

1. Open `assignment_3.py` using **IDLE 3.13** or any Python 3 interpreter.
2. Press `F5` or run the script from terminal:

```bash
python assignment_3.py

## Expected Output

Q1: Gaussian Elimination Solution:
[2, -1, 1]

Q2: LU Factorization
Determinant of A: 39.0

L matrix:

[1.0, 0.0, 0.0, 0.0]
[2.0, 1.0, 0.0, 0.0]
[3.0, 4.0, 1.0, 0.0]
[-1.0, -3.0, 0.0, 1.0]

U matrix:

[1.0, 1.0, 0.0, 3.0]
[0.0, -1.0, -1.0, -5.0]
[0.0, 0.0, 3.0, 13.0]
[0.0, 0.0, 0.0, -13.0]

## Checks if a matrix is diagonally dominant.

Q3: Diagonal Dominance
Is diagonally dominant? No

## Checks if a symmetric matrix is positive definite using Cholesky decomposition.
Q4: Positive Definiteness
Is positive definite? Yes
