/* This is a simple app which demonstrates the use of google maps flutter package. */
/*Steps to take before implementing this:
1: Navigate to <your-project>android>app>build.gradle file and update code on below line. 
Change Compile SDK Version
android {
    compileSdkVersion 31
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
also change the minimum sdk version
defaultConfig {
    // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
    applicationId "com.example.google_maps"
    minSdkVersion 20 //changed
    targetSdkVersion 30
    versionCode flutterVersionCode.toInteger()
    versionName flutterVersionName
}
 
2. Add API Key to Android Manifest File
Navigate to android > app > src > main > AndrodManifest.xml file and add the below code in the manifest tag. 
Make sure to add your Google Maps API key in the value. 
The Api key can be generated from google console after you setup your project there and enable google map sdk. 
<meta-data android:name="com.google.android.geo.API_KEY"
        android:value="Enter your API key here"/>
//this step is mendetory if you want to get user's location thru geolocator, if you are not planning on doing that, then skip this step.
3. Add the Following Permissions to the Android Manifest File
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION"/>
4. Add the Dependency to pubspec.yaml File of your project
dependencies:
    flutter: 
    google_maps_flutter: ^2.1.8 //could be any version
5. finally import the google_maps_flutter to use it, just like i have done in the example code below.
*/

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Google Maps Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late GoogleMapController
      controller; //will initialize this when the map is created

  //ps, you can get these values (latlang values) dynamically with geolocator package to show the location of the user...
  final LatLng paris = const LatLng(48.864716, 2.349014);
  final LatLng hyderabad = const LatLng(25.3960, 68.3578);
  //when the map will be created
  void init(GoogleMapController mapController) {
    controller = mapController;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Google Maps Flutter'),
        centerTitle: true,
      ),
      body: GoogleMap(
        mapType: MapType.normal,
        onMapCreated: init, // called when the map is created.
        initialCameraPosition: CameraPosition(
          target: paris,
          zoom: 11.0,
        ),
      ),
    );
  }
}
