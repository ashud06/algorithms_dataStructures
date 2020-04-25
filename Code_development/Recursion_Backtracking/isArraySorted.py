def isArraySorted(A):
    if len(A) == 1:
        return True
    return A[0]<=A[1] and isArraySorted(A[1:])

Array=[45,56,123,78,456,789]
if isArraySorted(Array):
    print("The array is sorted")
else:
    print("The array is not sorted")