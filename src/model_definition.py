"""
Decision Variables Definition:
The decision variables represent the quantities of products to be produced.
x1: Number of units of Product A
x2: Number of units of Product B
Both variables are non-negative integers.
"""


from pulp import LpVariable

# =========================
# Decision Variables
# =========================

# x1: Quantity of Product A
x1 = LpVariable("x1_Product_A", lowBound=0, cat="Integer")

# x2: Quantity of Product B
x2 = LpVariable("x2_Product_B", lowBound=0, cat="Integer")
