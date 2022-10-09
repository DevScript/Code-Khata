/*Interface: We force fully implement function.
In Abstract class we extend one class at a time,
but through implements we extend more than one classes.
In Interface we have normal fun, there has abstract fun.
*/

main() {
  var obj = class3();
  obj.fun1();
}

class class1 {
  fun1() {
    print("Function");
  }
}

class class2 {
  fun2() {}
}

class class3 implements class1, class2 {
  fun1() {
    print("Hello world");
  }

  fun2() {
    print("Hi Developer");
  }
}
