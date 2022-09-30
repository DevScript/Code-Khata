void sleepSort(int arr[], int n)
{
    // An array of threads, one for each of the elements
    // in the input array
    HANDLE threads[n];
  
    // Create the threads for each of the input array elements
    for (int i = 0; i < n; i++)
        threads[i] = (HANDLE)_beginthread(&routine, 0,  &arr[i]);
  
    // Process these threads
    WaitForMultipleObjects(n, threads, TRUE, INFINITE);
    return;
}
  
// Driver program to test above functions
int main()
{
    // Doesn't work for negative numbers
    int arr[] = {34, 23, 122, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
  
    sleepSort (arr, n);
  
    return(0);
}
