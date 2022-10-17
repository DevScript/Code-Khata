/*
 * The Map object is a simple key/value pair. Keys and values in a map may be of 
 * any type. A Map is a dynamic collection. In other words, Maps can grow and shrink 
 * at runtime.
 * Maps can be declared in two ways:
 * 1. Using a Map constructor
 * 2. Using Map Literals
 * 
 * Note:
 * -> Key has to be unique
 * -> Value can be duplicate
*/
void main() {
  // Using map constructor
  var squares = Map();
  squares['1'] = 1;
  squares['2'] = 4;
  squares['3'] = 9;
  squares['4'] = 16;
  squares['5'] = 25;
  
//   print(squares);
  
  // print all keys
//   for(var key in squares.keys) {
//     print(key);
//   }
  
  // print all values
//   for(var value in squares.values) {
//     print(value);
//   }
  
  // print all key value pairs
//   squares.forEach((key, value) => print('Key: $key, value: $value'));
  
  print(squares.containsKey('3'));
  print(squares.isEmpty);
  print(squares.length);
  
  squares.remove('4');
  print(squares);
  
  // Using map literal
  var userMap = {
    'name' : 'Waqar Ali Siyal',
    'age' : 21,
    'rollNo' : '18SW82',
  };
  
//   print(userMap);
//   print(userMap['name']);
}
