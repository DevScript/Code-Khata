#include <iostream>
using namespace std;

// function declarations
void merge(int[], int, int, int);
void merge_sort(int[], int, int);

int main() {
    cout<<"Enter size: ";
    int n;
    cin>>n;
    int arr[n];
    cout<<"Enter n space-separated values: ";
    for(int i=0; i<n; i++)
        cin>>arr[i];
    // input done

    merge_sort(arr, 0, n-1); // sorting 

    cout<<"Sorted Array: ";
    for(int elem: arr)
        cout<<elem<<" ";
    cout<<endl;
    return 0;
}

void merge_sort(int arr[], int low, int high) {
    if(low < high) {
        int mid=low + (high-low)/2; // to partition the array into 2 halves
        merge_sort(arr, low, mid); // sorting the left half
        merge_sort(arr, mid+1, high); // sorting the right half
        merge(arr, low, mid, high); // merging both the halves
    }
}

void merge(int arr[], int low, int mid, int high) {
    int n1=mid-low+1, n2=high-mid; // size of left half & right half
    int a[n1], b[n2]; 

    for(int i=0; i<n1; ++i)
        a[i] = arr[low+i]; // filling the left half
    for(int i=0; i<n2; ++i)
        b[i] = arr[mid+1+i]; // filling the right half

    // merging the two arrays into the original array
    int i=0, j=0, k=low;   
    while(i<n1 && j<n2) {
        if(a[i] < b[j])
            arr[k++] = a[i++];
        else
            arr[k++] = b[j++];
    }

    while(i < n1)
        arr[k++] = a[i++];
    while(j < n2)
        arr[k++] = b[j++];
}