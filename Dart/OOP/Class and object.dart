main() {
  print("hello");

  //  fun(); not run because we neend to make object

  var obj = new class1(); //object of class
  obj.fun(); //call class's function through object

  print(obj.name); //accessing variable from class
  obj.name2 = 'kanwal'; //pass value through object
  obj.fun();

  var obj2 = new class1();
  obj.name2 = 'How are You';
  obj.fun(); //same function but pass different values.
}

//creating the class
class class1 {
  var name2;

  var name = "hifza";
  fun() {
    print("function of class" + name2);
  }
}
