void main() {
//Abstract class
/* => Forcefully use function of class that extend.
    e.g class 2 must use funcation of class 1 (abstract class)
   => Define class by abstract keyword
   => Using extend keyword
   => Abstract class has both normal and abstract function   
   => No object of abstract class
   => Abstract function: Function that child class must use
   => Multi-level inheritance doesn't accessable 
   */

  var obj = new class2(); //object of abstract class not made
  obj.fun1();
}

abstract class class1 {
  fun1(); //Abstract funcation
  fun2() {
    print("normal funcation");
  }
}

class class2 extends class1 {
  //Defination of abstract funcation
  fun1() {
    print("abstract function defination");
  }
}
