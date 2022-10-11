Future<void> deleteuser(String id) {
  return user
      .doc(id)
      .delete(); // when we store data by our id then use set method
}
