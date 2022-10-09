import 'package:flutter/material.dart';

// the main advantage of using ListView or ListView.Builder() is that it renders only visible items on the screen
// which is a good approach instead of using Column, when you have to render the same widget nth number of times.

class ListViewBuilderExample extends StatelessWidget {
  List<int> randomNumbers = [
    1,
    5,
    4,
    6,
    7,
    4,
    7,
    9,
    2,
    8,
    10,
    2,
    3,
    68,
    69,
    114,
    37
  ];
  ListViewBuilderExample({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(
          child: Text('ListView Builder Example'),
        ),
        automaticallyImplyLeading: false,
      ),
      body: SafeArea(
        child: ListView.builder(
          padding: EdgeInsets.all(16),
          itemCount:
              randomNumbers.length, //no: of items the listview will contain
          itemBuilder: (BuildContext context, int index) {
            return Card(
              //i got a bit creative in using colors, basically [Colors.primaries] is a list which contains some of the primaries colors,
              //i have just played around with these colors, i.e using their different shades, opacities etc...
              color: Colors
                  .primaries[randomNumbers[index] % Colors.primaries.length]
                  .shade100,
              child: ListTile(
                contentPadding: EdgeInsets.all(16),
                leading: Container(
                  height: 50,
                  width: 50,
                  decoration: BoxDecoration(
                      color: Colors
                          .primaries[
                              randomNumbers[index] % Colors.primaries.length]
                          .shade900,
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.15),
                          spreadRadius: 5,
                          blurRadius: 7,
                          offset: Offset(0, 1),
                        ),
                      ]),
                ),
                title: Text(
                  "Item #${randomNumbers[index]}",
                  style: TextStyle(
                    color: Colors
                        .primaries[
                            randomNumbers[index] % Colors.primaries.length]
                        .shade900,
                    fontSize: 24,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
