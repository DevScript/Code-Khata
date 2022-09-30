'''
This function partitions a[] in three parts
   a) a[first..start] contains all elements smaller than pivot
   b) a[start+1..mid-1] contains all occurrences of pivot
   c) a[mid..last] contains all elements greater than pivot
    
'''
def partition(arr, first, last, start, mid):
     
    pivot = arr[last]
    end = last
     
    # Iterate while mid is not greater than end.
    while (mid[0] <= end):
         
        # Inter Change position of element at the starting if it's value is less than pivot.
        if (arr[mid[0]] < pivot):
             
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
             
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
             
        # Inter Change position of element at the end if it's value is greater than pivot.
        elif (arr[mid[0]] > pivot):
             
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
             
            end = end - 1
             
        else:
            mid[0] = mid[0] + 1
 
# Function to sort the array elements in 3 cases
def quicksort(arr,first,last):
    # First case when an array contain only 1 element
    if (first >= last):
        return
     
    # Second case when an array contain only 2 elements
    if (last == first + 1):
         
        if (arr[first] > arr[last]):
             
            arr[first], arr[last] = arr[last], arr[first]
             
            return
 
    # Third case when an array contain more than 2 elements
    start = [first]
    mid = [first]
 
    # Function to partition the array.
    partition(arr, first, last, start, mid)
     
    # Recursively sort sublist containing elements that are less than the pivot.
    quicksort(arr, first, start[0] - 1)
 
    # Recursively sort sublist containing elements that are more than the pivot
    quicksort(arr, mid[0], last)
 
# Code Start from here
arr = [4,9,4,4,1,9,4,4,9,4,4,1,4]
 
# Call the quicksort function.
quicksort(arr,0,len(arr) - 1)
 
# print arr after sorting the elements
print(arr)
