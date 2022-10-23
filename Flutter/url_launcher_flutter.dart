// about
/* it is simple app that demonstrate the use of url_launcher package which is used to launch email, sms, telephone, web & files too */

// note:

/* Steps to take before running this:
1. add dependency of url_launcher in the pubspec.yaml file of your project
    url_launcher: ^6.1.6

2. add some configuration in your <your_project>/android/app/src/main/AndroidManifest.xml file
after the application tag ends.., inside the manifest tag add these lines (queries)
        
    </application>
      .
      .
      .
        <!-- Provide required visibility configuration for API level 30 and above -->
    <queries>
    <!-- If your app checks for SMS support -->
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="sms" />
    </intent>
    <!-- If your app checks for call support -->
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="tel" />
    </intent>
    <!-- If your app checks for mail support -->

    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="mailto" />
    </intent>
    <!-- If your app checks for web url support -->
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="https" />
    </intent>
    </queries>

3. finally import the url_launcher package to use it just like i have in the example code below.

 */

import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

void main() => runApp(const MyApp());

//this function will remove the "+" signs caused by spaces in the key and value of query map.
encodeQueryParameters(Map<String, String> map) {
  return map.entries
      .map((MapEntry<String, String> e) =>
          '${Uri.encodeComponent(e.key)}=${Uri.encodeComponent(e.value)}')
      .join('&');
}

//send mail without any query i.e without default subject and body
_sendMail() async {
  var url = Uri.parse("mailto:herculesgamersoomro@gmail.com");
  try {
    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  } catch (e) {
    rethrow;
  }
}

//send mail with any queries
_sendMailWithBody() async {
  final Uri url = Uri(
    scheme: 'mailto',
    path: 'herculesgamersoomro@gmail.com"',
    query: encodeQueryParameters(<String, String>{
      'subject': 'Feedback from user',
      'body': 'Give your feedback here:'
    }),
  );
  if (await canLaunchUrl(url)) {
    await launchUrl(url);
  } else {
    throw ('Could not launch $url');
  }
}

_sendSms() async {
  var url = Uri.parse("sms:69696969");
  try {
    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  } catch (e) {
    rethrow;
  }
}

_sendSmsWithBody() async {
  // var url = Uri.parse("sms:966738292");
  final url = Uri(
    scheme: 'sms',
    path: '696969',
    queryParameters: <String, String>{
      'body': 'Give your feedback here:',
    },
  );
  try {
    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  } catch (e) {
    rethrow;
  }
}

_call() async {
  final url = Uri(
    scheme: 'tel',
    path: '696969',
  );
  try {
    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  } catch (e) {
    rethrow;
  }
}

_redirectToWebPortal() async {
  final url = Uri(
    scheme: 'https',
    path: 'github.com/atifsoomro114',
  );
  try {
    if (await canLaunchUrl(url)) {
      await launchUrl(url);
    }
  } catch (e) {
    rethrow;
  }
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: Scaffold(
        backgroundColor: Colors.deepPurple.shade100,
        appBar: AppBar(
          title: const Text(
            'Url_launcher_Example',
            style: TextStyle(
              color: Colors.white,
            ),
          ),
          centerTitle: true,
        ),
        body: SafeArea(
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                const Spacer(),
                Text(
                  'Give Feedback',
                  style: TextStyle(
                    color: Colors.deepPurple,
                    fontSize: 32,
                    decoration: TextDecoration.underline,
                    decorationColor: Colors.deepPurple.shade500,
                    decorationThickness: 2,
                  ),
                ),
                const Spacer(),
                TextButton.icon(
                  onPressed: _sendMail,
                  icon: const Icon(Icons.mail),
                  label: const Text('Feedback via Mail'),
                ),
                TextButton.icon(
                  onPressed: _sendMailWithBody,
                  icon: const Icon(Icons.mail),
                  label: const Text('Feedback via Mail with subject & body'),
                ),
                TextButton.icon(
                  onPressed: _sendSms,
                  icon: const Icon(Icons.sms),
                  label: const Text('Feedback via SMS'),
                ),
                TextButton.icon(
                  onPressed: _sendSmsWithBody,
                  icon: const Icon(Icons.sms),
                  label: const Text('Feedback via SMS with body'),
                ),
                TextButton.icon(
                  onPressed: _call,
                  icon: const Icon(Icons.phone),
                  label: const Text('Helpline'),
                ),
                TextButton.icon(
                  onPressed: _redirectToWebPortal,
                  icon: const Icon(Icons.wordpress),
                  label: const Text('Our Website'),
                ),
                const Spacer(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
