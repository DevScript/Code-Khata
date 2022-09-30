"""A typical recursive implementation of Quicksort for array """
   
""" This function takes last element as pivot, 
   places the pivot element at its correct 
   position in sorted array, and places all 
   smaller (smaller than pivot) to left of
   pivot and all greater elements to right 
   of pivot 
"""
  
"""
 i --> is the first index in the array
 x --> is the last index in the array
 tmp --> is a temporary variable for swapping values (integer)
"""
# array arr, integer l, integer h
def  partition (arr, l, h):
    x = arr[h]
    i = (l - 1)
    for j in range(l, h):
        if (arr[j] <= x):
            i +=1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
  
    tmp = arr[i + 1]
    arr[i + 1] = arr[h]
    arr[h] = tmp
    return(i + 1)
  
"""
A --> Array to be sorted,
l --> Starting index, 
h --> Ending index
"""
  
# array A, integer l, integer h
def quickSort(A, l, h):
    if (l < h):
        p = partition(A, l, h) # pivot index
        quickSort(A, l, p - 1) # left
        quickSort(A, p + 1, h) # right
