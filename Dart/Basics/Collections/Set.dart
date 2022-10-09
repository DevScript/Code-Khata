void main() {
  //Set: Store data in unorder way, and can't store duplicate data

  Set sarr = Set.from([2, 3, 2, 1]);

  for (int x in sarr) {
    print(x);
  }

  print(sarr.contains(10));

  //List
  var arr = ['Geeks', 'For', 'Geeks'];

//   sarr.remove(20);
//   sarr.isEmpty; //is empty or not
//   sarr.length; //to find length
//   sarr.clear; //full array remove

  // Printing List
  print(arr);

  // Declaring set with repeated value
  var sarr2 = <String>{'Geeks', 'For', 'Geeks'};

  // Printing Set
  print(sarr2);

  /*In set, tranditional loop not usecause no order of data,
   so not know indexes and we get data through index in traditional for loop*/
}
