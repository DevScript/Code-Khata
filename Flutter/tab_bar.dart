import 'package:flutter/material.dart';

class TabBarExample extends StatelessWidget {
  const TabBarExample({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    //in order to make tabBar work we have to wrap the scaffold with DefaultTabController i.e making the DefaultTabController as the direct child of home of a material app
    return DefaultTabController(
      length: 3, //number of tabs
      child: Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false, //removing the default back button
          title: const Center(
            child: Text('TabBar Example'),
          ),

          bottom: const TabBar(
            tabs: [
              Tab(
                icon: Icon(Icons.home),
                text: 'Home',
              ),
              Tab(
                icon: Icon(Icons.star_outline_sharp),
                // text: 'Stared Repos', //you can also chose to not add any text description of the tab
              ),
              Tab(
                icon: Icon(Icons.verified_user),
                text: "Merged PR's",
              ),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: const [
                Spacer(),
                Icon(Icons.settings),
                Spacer(),
                Text('You can also put custom widgets inside the TabBarView'),
                Spacer(),
              ],
            ),
            const Tab(
              //note, you can either put a text property or the child property in the Tab widget
              text: 'Stared Repos',
              // child: Center(
              //   child: Icon(Icons.star_outline_sharp),
              // ),
            ),
            const Tab(
              icon: Icon(Icons.verified_user),
              text: "Merged Pull Requests",
            ),
          ],
        ),
      ),
    );
  }
}
