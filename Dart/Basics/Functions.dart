// Functions   : code put in functions that are require again and again.

/*Expression(fat arrow), 
  parameter, 
  optional, 
  Named*/

main() {
  funName(); //calling default function
  //calling parameterize function
  var x = parFun(20, 10); //calling parametrize function
  print(x);
//fat expression
  var y = fatexp(40, 20);
  print(y);

//calling optional parameters
  opFun(2);

// namedPara(10,z:20,y:40);
}

//Default function
funName() {
  print("Function"); //define function here
  //function must return value, here return null
}

//parameterize function

parFun(int a, int b) {
  print(a + b);

  return a + b;

  //return 'Hello' , error because it return int value
}

//EXPRESSION

/*fatexp(int a, int b) {
   var r = (a+b);
   return r;
 }*/
fatexp(int x, int y) =>
    (x + y); //dont neend to write return, it automatically return the value

//optional parameters
opFun(int x, [int y = 10]) {
  print(x + y);
} //default value is 10

// namedPara(int x, {int y, int z}){

//   print(x);
//   print(y);
//   print(z);

// }