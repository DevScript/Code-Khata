//polymorphism: same operation may behave different in different class
//same function name, but behave different

main() {
  var obj = new class2();
  obj.fun1();
}

class class1 {
  var name = "hifza";
  fun1() {
    print("class1");
  }
}

class class2 extends class1 {
  var name = "kanwal";
  fun1() {
    super.fun1(); //first call parent class's function
    print("class2");
    print(name);
    print(super.name);
  }
}
