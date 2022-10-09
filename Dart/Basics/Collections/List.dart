void main() {
// LIST
  var larr = [3, 2, 4, 7];

  print(larr[1]);

  //change the value
  larr[1] = 100;
  print(larr[1]);

  //remove any value
  larr.remove(100);
  larr.removeAt(2);

  //   larr.clear();
  print(larr[1]);

  //Reterive full data through Loops:

  //for loop

  for (int x in larr) {
    print("loop");
    print(x);
  }

  //for each

  larr.forEach((x) => print(x));

  //traditional for loop

  for (int x = 0; x < 4; x++) {
    print(larr[x]);
  }
}
