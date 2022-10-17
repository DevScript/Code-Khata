// The values of parent scope variables can be modified within a closure

void main() {
  // A closure is a function that has access to the parent scope, even after the
  // scope has closed
  String msg = 'Hello';
  Function greet = () {
    msg = 'Good Night';
    print(msg);
  };
  greet();

  // A closure is a function object that has access to variables in its lexical scope, even
  // when the function is used outside of its original scope
  Function outsideFunc = () {
    String msg = 'Outside Func';
    Function insideFunc = () {
      msg = 'Inside Func';
      print(msg);
    };
    return insideFunc;
  };

  Function funcObj = outsideFunc(); // inside Func
  funcObj(); // Calling insideFunc
}
