import numpy as np
from numpy.random import randn
randn()

answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
print(x)
print(answer)

answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)

#nested statements

answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    if x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)

#chain
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
    answer = "Between -1 and 1"
else:
    answer = "Less than -1"
print(x)
print(answer)