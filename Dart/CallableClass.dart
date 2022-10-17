/* 
 * Dart allows the user to create a callable class which allows the 
 * instance of the class to be called as a function. To allow an 
 * instance of your Dart class to be called like a function, implement 
 * the call() method. 
 */
void main() {
  Student std1 = Student();
  int age = std1('Waqar Ali Siyal', 21);
  print(age);
}

class Student {
  int call(String name, int age) {
//     print('This is call method');
//     print('$name $age');
    return age;
  }
}
