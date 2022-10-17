/* 
 * List is a collection of items. A list is referenced by a variable name. The items in the 
 * list can be accessed using index. Index starts with 0.
 * Types of List
 * 1. Fixed Length List
 * 2. Growable List
 * In this video we will cover Fixed Length List
*/ 
void main() {
  // Understand List
  // 5 elements, index from 0 - 4
  // 8 elements, index from 0 - 7
  // 0 - First Element
  // 1 - Second Element
  // and so on upto (length of list - 1)
//   var oddNums = List(5);
//   print(oddNums[0]);
  var oddNums = List<int>.filled(5, 0);
//   oddNums.length = 10;  // error
//   oddNums.add(1);       // error
  oddNums[0] = 1;
  oddNums[1] = 3;
  oddNums[2] = 5;
  oddNums[3] = 7;
  oddNums[4] = 9;
  
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
  oddNums.forEach((element) => print(element));
}
