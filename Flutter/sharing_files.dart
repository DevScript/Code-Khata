//*********About*********//
// It is a simple application which demonstrates the use of shared_plus package
// along with image_picker in order to share files/images.
//*********Note*********//

// Firstly, Make sure you have added the packages in pubspec.yaml file
// flutter:
//     sdk: flutter
//   image_picker: ^0.8.6
//   share_plus: ^4.5.3

//*********Code*********//
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:share_plus/share_plus.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: const Home(),
    );
  }
}

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final ImagePicker imagePicker = ImagePicker();
  XFile? pickedImage;
  String message = '';
  String subject = '';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Share Plus Working'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        physics: const BouncingScrollPhysics(),
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'This is a demonstration of share plus package',
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headlineSmall!.copyWith(
                      color: Colors.deepPurple.shade600,
                      fontWeight: FontWeight.w600,
                      height: 1.5,
                    ),
              ),
              const SizedBox(height: 48),
              Divider(
                color: Colors.deepPurple.shade900,
                thickness: 4,
                height: 48,
                indent: MediaQuery.of(context).size.width * 0.2,
                endIndent: MediaQuery.of(context).size.width * 0.2,
              ),
              TextField(
                decoration: const InputDecoration(
                  labelText: 'Message',
                  hintText: 'Write Something',
                ),
                onChanged: (text) {
                  setState(() {
                    message = text;
                  });
                },
              ),
              const SizedBox(
                height: 24,
              ),
              TextField(
                decoration: const InputDecoration(
                  labelText: 'Subject',
                  hintText: 'Write your subject',
                ),
                onChanged: (text) {
                  setState(
                    () {
                      subject = text;
                    },
                  );
                },
              ),
              const SizedBox(height: 24),
              Builder(
                builder: (BuildContext context) {
                  return IconButton(
                    disabledColor: Colors.deepPurple.shade100,
                    color: Colors.deepPurple.shade900,
                    onPressed: message.isEmpty
                        ? null
                        : () {
                            onShare(context, message, subject);
                          },
                    icon: const Icon(Icons.send),
                  );
                },
              ),
              Divider(
                color: Colors.deepPurple.shade900,
                thickness: 4,
                height: 48,
                indent: MediaQuery.of(context).size.width * 0.2,
                endIndent: MediaQuery.of(context).size.width * 0.2,
              ),
              const SizedBox(height: 24),
              pickedImage != null
                  ? const ChangeImageToolTip()
                  : const SizedBox(),
              const SizedBox(height: 24),
              GestureDetector(
                onTap: () async {
                  await showDialog(
                    context: context,
                    builder: (context) {
                      return ImagePickerDialog(
                        galleryFunction: () {
                          pickImageFromGallery();
                          // if (pickedImage != null) {
                          Navigator.of(context).pop();
                          // }
                        },
                        cameraFunction: () {
                          pickImageFromCamera();
                          // if (pickedImage != null) {
                          Navigator.of(context).pop();
                          // }
                        },
                      );
                    },
                  );
                },
                child: Container(
                  child: pickedImage == null
                      ? const DefaultImageWidget()
                      : Image.file(
                          File(pickedImage!.path),
                        ),
                ),
              ),
              const SizedBox(height: 24),
              Builder(
                builder: (BuildContext context) {
                  return IconButton(
                    disabledColor: Colors.deepPurple.shade100,
                    color: Colors.deepPurple.shade900,
                    onPressed: pickedImage == null
                        ? null
                        : () {
                            onShareFile(context);
                          },
                    icon: const Icon(Icons.share),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

// ******* Utility Functions ********

  void onShare(BuildContext context, String message, String subject) async {
    final box = context.findRenderObject() as RenderBox?;
    // print('on share called');
    await Share.share(
      message,
      subject: subject,
      sharePositionOrigin: box!.localToGlobal(Offset.zero) & box.size,
    );
  }

  void onShareFile(BuildContext context) async {
    final box = context.findRenderObject() as RenderBox?;
    // print('on share called');
    await Share.shareXFiles(
      [
        XFile(pickedImage!.path),
      ],
      subject: '',
      text: '',
      sharePositionOrigin: box!.localToGlobal(Offset.zero) & box.size,
    );
  }

  void pickImageFromGallery() async {
    XFile? image = await imagePicker.pickImage(
      source: ImageSource.gallery,
      maxWidth: 1080,
      maxHeight: 1080,
    );
    if (image != null) {
      setState(() {
        pickedImage = image;
      });
    }
  }

  void pickImageFromCamera() async {
    XFile? image = await imagePicker.pickImage(
      source: ImageSource.camera,
      maxWidth: 1080,
      maxHeight: 1080,
    );
    if (image != null) {
      setState(() {
        pickedImage = image;
      });
    }
  }
}

// ******* Constant Widgets ********

//it will be shown when there is no image selected.
class DefaultImageWidget extends StatelessWidget {
  const DefaultImageWidget({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.deepPurple.shade100,
        boxShadow: [
          BoxShadow(
            blurRadius: 7,
            color: Colors.deepPurple.shade300,
            spreadRadius: 2,
            offset: const Offset(3, 2),
          )
        ],
      ),
      height: 100,
      width: double.infinity,
      child: Center(
        child: Text(
          'click me to pick a new image to share'.toLowerCase(),
          style: Theme.of(context).textTheme.headline6!.copyWith(
              color: Colors.deepPurple.shade300, fontStyle: FontStyle.italic),
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}

//it will be shown when the user clicks on the default pick me continaer or image

class ImagePickerDialog extends StatelessWidget {
  final void Function() galleryFunction;
  final void Function() cameraFunction;

  const ImagePickerDialog(
      {Key? key, required this.galleryFunction, required this.cameraFunction})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      backgroundColor: Colors.deepPurple.shade100
          .withOpacity(0.8), //for cool transparent BG.
      insetPadding: const EdgeInsets.symmetric(horizontal: 48),
      actionsAlignment: MainAxisAlignment.spaceEvenly,
      title: Text(
        'Pick Image'.toUpperCase(),
        textAlign: TextAlign.center,
        style: TextStyle(
          color: Colors.deepPurple.shade900,
          letterSpacing: 1.6,
        ),
      ),
      content: Text(
        'You can click a new Image or you can select from the gallery',
        textAlign: TextAlign.center,
        style: TextStyle(
          color: Colors.deepPurple.shade900,
          height: 1.7,
          fontStyle: FontStyle.italic,
        ),
      ),
      actions: [
        IconButton(
          onPressed: cameraFunction,
          iconSize: 32,
          icon: const Icon(
            Icons.camera_alt_outlined,
            size: 32,
          ),
          color: Colors.deepPurple,
          splashColor: Colors.deepPurple.shade100,
        ),
        IconButton(
          onPressed: galleryFunction,
          iconSize: 32,
          icon: const Icon(
            Icons.photo,
          ),
          color: Colors.deepPurple,
          splashColor: Colors.deepPurple.shade100,
        ),
      ],
    );
  }
}

//it will be shown when the image is already picked/selected to let the user know that they can change it.

class ChangeImageToolTip extends StatelessWidget {
  const ChangeImageToolTip({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      fit: StackFit.passthrough,
      //for showing/displaying the overflow
      clipBehavior: Clip.none,
      //
      children: [
        Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(4),
            border: Border.all(
              color: Colors.deepPurple.shade400,
              width: 4,
            ),
          ),
          child: Padding(
            padding: const EdgeInsets.all(12.0),
            child: Text(
              'You can change the image by clicking on it',
              style: Theme.of(context).textTheme.bodyText1!.copyWith(
                    color: Colors.deepPurple.shade900,
                    height: 1.3,
                    fontSize: 14,
                    fontStyle: FontStyle.italic,
                  ),
              textAlign: TextAlign.center,
            ),
          ),
        ),
        Positioned(
          top: -36.2,
          left: 0,
          right: 0,
          child: Icon(
            Icons.lightbulb_circle_rounded,
            color: Colors.deepPurple.shade400,
            size: 44,
          ),
        ),
      ],
    );
  }
}
