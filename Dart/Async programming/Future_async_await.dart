//Async-programming where we can move to another task before the previous one finishes.
//Future, async, await

main() async {
  print("Main");
  await futureFun();
  print("Last Statement");
}

Future<void> futureFun() async {
  Future.delayed(Duration(seconds: 5), () {
    print("Future Function");
  });
}
