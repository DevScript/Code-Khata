import 'dart:convert';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:pinput/pinput.dart';

import 'Component.dart';
import 'Homescreen.dart';

class verifycode extends StatefulWidget {
  final String verificationId;
  const verifycode({super.key, required this.verificationId});

  @override
  State<verifycode> createState() => _verifycodeState();
}

class _verifycodeState extends State<verifycode> {
  bool loading = false;

  var code = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Verification"),
        backgroundColor: bcolor,
      ),
      body: Form(
          child: Column(
        children: [
          SizedBox(
            height: 70,
          ),
          Text(
            "Code is sent to your number",
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 18,
            ),
          ),
          SizedBox(
            height: 70,
          ),
          Padding(
            padding: const EdgeInsets.all(40),
            child: Pinput(
              pinAnimationType: PinAnimationType.fade,
              length: 6,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.center,
              defaultPinTheme: PinTheme(
                height: 50,
                textStyle: GoogleFonts.urbanist(
                    fontSize: 24,
                    color: Colors.black,
                    fontWeight: FontWeight.w700),
                width: 50,
                decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.white,
                    border: Border.all(color: bcolor, width: 2)),
              ),
              onChanged: (value) async {
                final tokencredidential = PhoneAuthProvider.credential(
                    verificationId: widget.verificationId, smsCode: code);

                try {
                  await FirebaseAuth.instance
                      .signInWithCredential(tokencredidential);
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              homescreen(name: 'Welcome Again')));
                } catch (e) {
                  print(e);

                  Navigator.pop(context);
                }
                code = value;
              },
            ),
          ),
          SizedBox(
            height: 40,
          ),
          roundbutton(
              title: "Verify",
              tapfun: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => homescreen(name: '')));
                print(code);
              }),
        ],
      )),
    );
  }
}
