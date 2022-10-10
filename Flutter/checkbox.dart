import 'package:flutter/material.dart';

class WCheckbox extends StatefulWidget {
  const WCheckbox({Key? key}) : super(key: key);

  @override
  State<WCheckbox> createState() => _WCheckboxState();
}

class _WCheckboxState extends State<WCheckbox> {
  bool? games = false;
  bool? movies = true;
  bool? sports = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Spacer(),
              Text(
                'Select your hobbies',
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headline4,
              ),
              const Spacer(),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text('Games'),
                  Checkbox(
                      // fillColor: MaterialStateProperty(),
                      checkColor: Colors.white,
                      activeColor: Colors.amber,
                      value: games,
                      onChanged: (bool? value) {
                        setState(() {
                          games = value;
                        });
                      })
                ],
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text('Movies'),
                  Checkbox(
                      value: movies,
                      //this onchange function will change the value of the
                      onChanged: (bool? value) {
                        setState(() {
                          movies = value;
                        });
                      })
                ],
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text('Sports'),
                  Checkbox(
                    value: sports,
                    onChanged: (bool? value) {
                      setState(() {
                        sports = value;
                      });
                    },
                  ),
                ],
              ),
              const Spacer(),
            ],
          ),
        ),
      ),
    );
  }
}
