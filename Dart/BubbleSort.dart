//Dart program to sort a list using bubble sort


//Method to sort the list, where the list is passed as an argument
void BubbleSort(List list) {     //Function to do the sorting, where the list is passed as an argument
  if(list.length == 0) return;   //Checks if the list has elements or not. If no element present, it exits the function

  int n = list.length;
  int i, j;
  for(i=0;i<n;i++) {
    for(j=0;j<n-i-1; j++) {     //last i elements are already sorted. -1 is done as indexing of list starts from 0
      if(list[j]>list[j+1]) {   //Switch '>' to '<' to sort the list in descending order
        swap(list, j);
      }
    }
  }
}

//Utility function
//Method to swap jth and j+1th element of the array using a third variable
void swap(List list, int j) {
  int temp = list[j];
  list[j]=list[j+1];
  list[j+1]=temp;
}

//Driver code
void main() {
  List list = [3,7,1,9,4,6,8];  //a list can be taken as an input also.
  BubbleSort(list);  
  print("Sorted list is: $list");
}