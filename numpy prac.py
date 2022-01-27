import numpy as np
arr = np.array([[12,3,34,1], [32,0,5,1], [34,5,6,6]])
print(arr.sum(axis= 0))


print(arr.T)

ft = arr.flat
for item in ft:
    print(item)