//Dart program to sort a list using Selection sort

//Method to sort the list, passed as an argument
void SelectionSort(List list) {
  if(list.length == 0) return;    //Check if the list is empty, if so, exits the code.

  int n = list.length;
  int i, j;

  //Move the boundary of the unsorted array, as every element before i will be sorted.
  for(i=0;i<n-1;i++) {

    //Find minimum element in the unsorted list
    int minele = i;
    for(j=i+1;j<n; j++) {
      if(list[j]<list[minele]) {  //Switch '<' to '>' to sort the list in descending order
        minele = j;               //storing the index of the minimum element of the unsorted list
      }
    }

    //swap the minimum element with the first element of the unsorted list
    if(minele != i) {
      swap(list, i, minele);
    }
  }
}


//Utility function
//Method to swap the list elements at index i and j
void swap(List list, int i, int j) {
  int temp = list[i];
  list[i]=list[j];
  list[j]=temp;
}

//Driver code
void main() {
  List list = [3,7,1,9,4,6,8];    //List also can be taken from the user.
  SelectionSort(list);  
  print("Sorted list is: $list");
}