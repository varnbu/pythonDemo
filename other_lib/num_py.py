import numpy as np

arr1 = np.array([2, 3, 4])
print(arr1)
print(arr1.dtype)

arr2 = np.array([1.2, 3.4, 5.6])
print(arr2)
print(arr2.dtype)

print(arr1 + arr2)

print(arr2 * 10)

data = [
    [1, 2, 3],
    [5, 6, 7]
]

arr3 = np.array(data)
print(arr3)
print(arr3.dtype)
