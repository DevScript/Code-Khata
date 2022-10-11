Future<void> updateuser(id, var name, var rollNo) {
  // String name = "Kanwal";
  return user.doc(id).update({
    'name': name,
    'rollNo': rollNo,
  }); // when we store data by our id then use set method
}
