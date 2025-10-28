# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
# ]
# ///

# Day 24: Introduction to NumPy
import numpy as np
# Install NumPy

# Arrays, array operations

# Indexing, slicing, reshaping
# arr = np.array([[[1, 2, 3], [2, 5, 6]], [[1, 2, 3], [3, 5, 6]]], ndmin = 5)
# print(arr[1][1])
# print(arr[1,1:3])
# print(arr.ndim)

# Practice: Matrix operations, statistical calculations, array manipulation
def matrix():
    arr1 = np.array([[1,2],[4,5]])
    arr2 = np.array([[4,5],[7,8]])
    a3 = np.array([[1,2,3],[1,2,3]])
    a4 = np.array([[1,2,3],[1,2,3]])
    a5 = np.array([[1,2,3,4],[5,6,7,8]])
    a6 = np.array([[1,2,3,4],[5,6,7,8]])
    print("Matrix A:\n", arr1)
    print("Matrix B:\n", arr2)
    print("Matrix A x B:\n", np.dot(arr1, arr2))
    print("Matrix a5 x a6:\n", np.dot(a5, a6.T))
    print("Matrix A + B: ", a3 + a4)
    print("Matrix A * B: ", a3 * a4)
    print("Sum: ", np.sum(a5))
    print("Mean: ", np.mean(arr1))
    print("Median: ", np.median(a5))
    print("Standerd deviation: ", np.std(a5))
    print("Variance: ", np.var(a5))
    print("Minimum: ", np.min(a5))
    print("Maximum: ", np.max(a5))
    print("Row wish sum: ", np.sum(a5, axis =1))
    print("Colim wish sum: ",np.sum(a5, axis= 0))

matrix()
