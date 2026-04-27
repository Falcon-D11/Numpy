import numpy as np
prices=np.array([100,200,300])
discout=10
final_price=prices-(prices*discout/100)
print(final_price)
"""
Broadcasting Rules

NumPy compares shapes from right to left.

Two dimensions are compatible if:

They are equal
OR
One of them is 1
"""

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([1,2,3])
result=matrix+vector
print(result)
