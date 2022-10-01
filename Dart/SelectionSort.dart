void BubbleSort(List list) {
  if(list.length == 0) return;

  int n = list.length;
  int i, j;
  for(i=0;i<n;i++) {
    for(j=i+1;j<n; j++) {
      if(list[i]>list[j]) {
        swap(list, i, j);
      }
    }
  }
}

void swap(List list, int i, int j) {
  int temp = list[i];
  list[i]=list[j];
  list[j]=temp;
}

void main() {
  List list = [3,7,1,9,4,6,8];
  BubbleSort(list);  
  print("Sorted list is: $list");
}