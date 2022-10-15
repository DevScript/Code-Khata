import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:get/get.dart';
import 'package:get/get_state_manager/get_state_manager.dart';
import 'package:social_login_buttons/social_login_buttons.dart';

class SignupView extends GetWidget {
  const SignupView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: SingleChildScrollView(
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(height: Get.mediaQuery.size.height * 0.05),
            Text("Sign Up", style: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 30, fontWeight: FontWeight.bold)),
            SizedBox(height: Get.mediaQuery.size.height * 0.05),
            Container(
                padding: EdgeInsets.all(Get.mediaQuery.size.width * 0.1),
                width: Get.mediaQuery.size.width * 0.9,
                decoration: BoxDecoration(
                    color: Get.theme.scaffoldBackgroundColor,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: Get.theme.shadowColor, width: 1),
                    boxShadow: [BoxShadow(color: Get.theme.shadowColor, blurRadius: 100, offset: const Offset(0, 0))]),
                child: Form(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      TextFormField(
                        style: TextStyle(color: Get.theme.colorScheme.secondary),
                        decoration: InputDecoration(
                          labelText: "First Name",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.colorScheme.secondary,
                            ),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          labelStyle: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 18),
                          floatingLabelStyle: TextStyle(color: Get.theme.primaryColor, fontSize: 18),
                        ),
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(height: Get.mediaQuery.size.height * 0.03),
                      TextFormField(
                        style: TextStyle(color: Get.theme.colorScheme.secondary),
                        decoration: InputDecoration(
                          labelText: "Last Name",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.colorScheme.secondary,
                            ),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          labelStyle: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 18),
                          floatingLabelStyle: TextStyle(color: Get.theme.primaryColor, fontSize: 18),
                        ),
                        keyboardType: TextInputType.name,
                      ),
                      SizedBox(height: Get.mediaQuery.size.height * 0.03),
                      TextFormField(
                        style: TextStyle(color: Get.theme.colorScheme.secondary),
                        decoration: InputDecoration(
                          labelText: "Email",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.colorScheme.secondary,
                            ),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          labelStyle: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 18),
                          floatingLabelStyle: TextStyle(color: Get.theme.primaryColor, fontSize: 18),
                        ),
                        keyboardType: TextInputType.emailAddress,
                      ),
                      SizedBox(height: Get.mediaQuery.size.height * 0.03),
                      TextFormField(
                        style: TextStyle(color: Get.theme.colorScheme.secondary),
                        decoration: InputDecoration(
                          labelText: "Password",
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.colorScheme.secondary,
                            ),
                          ),
                          focusedBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          enabledBorder: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(5.0),
                            borderSide: BorderSide(
                              color: Get.theme.primaryColor,
                            ),
                          ),
                          labelStyle: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 18),
                          floatingLabelStyle: TextStyle(color: Get.theme.primaryColor, fontSize: 18),
                        ),
                        obscureText: true,
                        keyboardType: TextInputType.visiblePassword,
                      ),
                      const SizedBox(height: 20),
                      ElevatedButton(
                          onPressed: () {},
                          // ignore: sort_child_properties_last
                          child: Text(
                            "Sign Up",
                            style: TextStyle(fontSize: Get.mediaQuery.size.width * 0.045),
                          ),
                          style: ButtonStyle(
                            backgroundColor: MaterialStateProperty.all(Get.theme.primaryColor),
                            minimumSize: MaterialStateProperty.all(Size(Get.mediaQuery.size.width, Get.mediaQuery.size.height * 0.08)),
                          )),
                      SizedBox(height: Get.mediaQuery.size.height * 0.01),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          TextButton(
                            child: Text("Forgot Password", style: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 12)),
                            onPressed: () {},
                          ),
                          const Text("|", style: TextStyle(fontSize: 12, color: Colors.grey)),
                          TextButton(
                            child: Text("Sign In", style: TextStyle(color: Get.theme.colorScheme.secondary, fontSize: 12)),
                            onPressed: () {
                              Get.toNamed("/login");
                            },
                          ),
                        ],
                      ),
                      SizedBox(height: Get.mediaQuery.size.height * 0.003),
                      const Text("OR", style: TextStyle(fontSize: 12, color: Colors.grey)),
                      SizedBox(height: Get.mediaQuery.size.height * 0.02),
                      SocialLoginButton(text: "Continue with Google", buttonType: SocialLoginButtonType.google, onPressed: () {}),
                      SizedBox(height: Get.mediaQuery.size.height * 0.02),
                      SocialLoginButton(text: "Continue with Facebook", buttonType: SocialLoginButtonType.facebook, onPressed: () {}),
                      SizedBox(height: Get.mediaQuery.size.height * 0.02),
                      getAppleButton()
                    ],
                  ),
                )),
            SizedBox(height: Get.mediaQuery.size.height * 0.03),
          ],
        ),
      ),
    ));
    throw UnimplementedError();
  }

  getAppleButton() {
    if (Platform.isIOS) {
      return SocialLoginButton(text: "Continue with Apple", buttonType: SocialLoginButtonType.apple, onPressed: () {});
    }
    return SizedBox(
      height: 0,
    );
  }
}
