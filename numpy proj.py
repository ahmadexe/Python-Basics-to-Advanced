import numpy as np
myar = np.array([[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1]])
print(myar)

x = myar.sum(axis=0)
print(x)
for item in x:
    if item % 2 == 0:
        print("The sum of this row is even")
    else:
        print("The sum of this row is odd")

y = myar.sum(axis=1)
print(y)
for item in y:
    if item % 2 == 0:
        print("The sum of the column is even") 
    else:
        print("The sum is odd")