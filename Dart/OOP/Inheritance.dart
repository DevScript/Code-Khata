//Inheritance : accessing properties from parent class
//when we call constructor of child class, automatically constructor of parent class call

main() {
  var obj = new class2();
  obj.fun1(); //Inherit fun of class1 by using extends keyword
  obj.fun2();
  var obj1 = new class3();
  obj.name;
}

class class1 {
  var name = "hifza";
  fun1() {
    print("Hi");
  }
}

class class2 extends class1 {
  fun2() {
    print(name);
  }
}

//Multi-level inheritance: class 3 inherit classs 2 and class 2 inherit class 1, and access fun();
class class3 extends class2 {}
