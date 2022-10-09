void main() {
//Map

  Map<String, String> marr = {'name': 'hifza', 'city ': 'abbottabad'};
  //add new value
  marr['email'] = 'hifzakanwal75@gmail.com';

  //for loop: just one value in one time
//get key
  for (String key in marr.keys) {
    print(key);
  }

  //get values

  for (String v in marr.values) {
    print(v);
  }

  //for each loop: get both value and key at a time
  marr.forEach((key, value) => print(key + value));

  marr.length;
  marr.clear();
  marr.isEmpty;
  marr.containsKey('name');
  marr.containsKey('hifza');
}
