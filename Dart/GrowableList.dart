/* 
 * List is a collection of items. A list is referenced by a variable name. The items in the 
 * list can be accessed using index. Index starts with 0.
 * Types of List
 * 1. Fixed Length List
 * 2. Growable List
 * In this video we will cover Growable List
*/ 
void main() {
  // Understand List
  // 5 elements, index from 0 - 4
  // 8 elements, index from 0 - 7
  // 0 - First Element
  // 1 - Second Element
  // and so on upto (length of list - 1)
  List<int> oddNums = [];
  oddNums.add(1);
  oddNums.add(3);
  oddNums.add(5);
  oddNums.add(7);
  oddNums.add(9);
//   print(oddNums.length);
//   print(oddNums);
  
//   oddNums.remove(3);
//   print(oddNums.length);
//   print(oddNums);
  
//   oddNums.removeAt(2);
//   print(oddNums.length);
//   print(oddNums);
  
//   oddNums.add(11);
//   print(oddNums);
  
//   oddNums.insert(1, 3);
//   oddNums.insert(3, 7);
//   print(oddNums);
  
//   oddNums.clear();
//   print(oddNums);
  
//   print(oddNums[3]);
  
  // Print all elements using for loop
//   for(int i=0; i<oddNums.length; i++) {
//     print(oddNums[i]);
//   }
  
  // Print all elements using for in loop
//   for(int element in oddNums) {
//     print(element);
//   }
  
  // Print all elements using for each loop
//   oddNums.forEach((element) => print(element));
  
  var weekDays = ['Monday', 'Tuesday', 'Wednesday'];
  weekDays.add('Thursday');
  weekDays.add('Friday');
  print(weekDays.length);
  print(weekDays);
}
