Future<void> adduser(var name, rollNo) async {
  print("Added");
  CollectionReference user = FirebaseFirestore.instance.collection('students');
  String uId = DateTime.now().microsecondsSinceEpoch.toString();
  // String uId = '7575';
  // String name = 'hifza';
//default random id set in firestore: return user.add({'uId': uId, 'name': name})
//set id is 7575
  return await user
      .doc(uId)
      .set({'uId': uId, 'name': name, 'rollNo': rollNo})
      .then((value) => Navigator.push(
          context, MaterialPageRoute(builder: ((context) => homescreen()))))
      .onError((error, stackTrace) => print("Error"));
}
