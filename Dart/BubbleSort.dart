void BubbleSort(List list) {
  if(list.length == 0) return;

  int n = list.length;
  int i, j;
  for(i=0;i<n;i++) {
    for(j=0;j<n-i-1; j++) {
      if(list[j]>list[j+1]) {
        swap(list, j);
      }
    }
  }
}

void swap(List list, int j) {
  int temp = list[j];
  list[j]=list[j+1];
  list[j+1]=temp;
}

void main() {
  List list = [3,7,1,9,4,6,8];
  BubbleSort(list);  
  print("Sorted list is: $list");
}