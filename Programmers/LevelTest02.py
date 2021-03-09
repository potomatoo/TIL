import numpy
def solution(arr1, arr2):
    arr1 = numpy.array(arr1)
    arr2 = numpy.array(arr2)
    arr3 = arr1.dot(arr2)
    arr3 = arr3.tolist()
    return arr3

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))



