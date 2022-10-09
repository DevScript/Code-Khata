void main() {
// Operators
  //Arthematic (+, -, /, *, %, ~/)

  var a = 30;
  var b = 20;

  print(a + b);
  print(a - b);
  print(a * b);
  print(a / b);
  print(a % b);
  print(a ~/ b);

  //Relational ( > < >= <= == != )
  // return true or false value

  print(a > b);
  print(a < b);
  print(a >= b);
  print(a <= b);
  print(a == b);
  print(a != b);

  //Test operators  (is is!)

  print(a is String);
  print(a is! String);

  ///Increment and decrement (sometime include in arthematic operators)
  print(
      a++); //still same as 30, because post increment give result in next line,
  //so,

  print(a); //now answer is 30+1 = 30

  //Assignment ( = += -= *= )

  var ao = 10;
  ao += 2; // ao = ao + 2;

  print(ao);

  //Logical operators ( || && ! )

  if (a == 30 && b == 10) {
    print('&&'); //because b is not equal to 10
  }

  if (a == 30 || b == 10) {
    print('||');
  }

  if (a != 20) {
    print('!');
  }

  //conditional ( ?: ?? )

  print(a > 20 ? 'A is greater than 20' : 'A is less than 20');

  //cascade Notation (..) .. want to perfome more than one operations at a time

  var c1 = "Hifza";

  print(c1.toLowerCase()..substring(2));

  //bitwise ( & | ~ ^ a<<b a>>b )

  /*its for bit
  e.g converting to bit
  
  128 64 32 16 8 4 2 1
  0   0  0  0  0 1 0 1 for 5
  0   0  0  0  0 1 1 1 for 7
  
   7 & 5 answer is 5 because there are common 1 in both 4 and 1 so 1 + 4 is 5
   | answer is 7 cause having at least one 1 , so 4 + 2 + 1 = 7
   ^ xOr answer is 2 because ouput where different (not same) as 2 has 0 and 1
   >> right shift move bit to right
   >> left shift move bit to left 
  */

  var bt1 = 7;
  var bt2 = 5;
  print("g");
  print(bt1 & bt2);
  print(bt1 | bt2);
  print(bt1 ^ bt2);
  print(bt1 >> bt2);
  print(bt1 << bt2);
}
