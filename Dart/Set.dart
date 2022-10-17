/* 
 * In Dart, Set is a unordered list of distinct values of same types. Set is 
 * much similar to an array but it is unordered and won’t allows duplicate elements, 
 * each value contained in a set is unique. You cannot get elements by index, since the
 * items are unordered.
 * There are two ways we can declare/initialize an empty set, use {} preceded by a 
 * type argument, or assign {} to a variable of type Set.
 * 1. var setName = <type>{};
 * 2. Set<type> setName = {};
 * Note: The syntax for map literals is similar to that for set literals. If you 
 * forget the type annotation with {} or with the variable it’s assigned to, 
 * then Dart would creates an Map object instead of Set.
*/ 
void main() {
  var oddNums = <int>{};
  oddNums.add(1);
  oddNums.add(3);
  oddNums.add(5);
  oddNums.add(7);
  
  oddNums.add(3);       // Duplicate entries are ignored
  
  print(oddNums);
  
  Set<int> evenNums = {2, 4, 6, 8, 4, 10};
  evenNums.add(12);
  print(evenNums);
  
  print(evenNums.contains(6));
  print(oddNums.contains(2));
  
  evenNums.remove(12);
  print(evenNums);
  
  print(evenNums.isEmpty);
  evenNums.clear();
  print(evenNums);
  print(oddNums.length);

  oddNums.addAll({9,11,13});
  print(oddNums);

  // Set from List
  var weekDays = ['Monday', 'Tuesday', 'Wednesday'];
  var weekDaysSet = Set.from(weekDays);
  print(weekDaysSet);
  weekDaysSet.add('Friday');
  weekDaysSet.add('Thursday');
  print(weekDaysSet);
}
