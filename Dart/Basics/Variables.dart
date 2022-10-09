void main() {
  /*  
   int
   double
   String
   bool
   List (like array)
   Map
   Dynamic
   */

//int
  int age = 20;
  print(age);

//double
  double weight = 20.3; //for decimale
  print(weight);

//String
  String name = 'hifza';
  print(name);

//bool
  bool isCoding = true;
  print(isCoding);

  //List: List is like array, collection of different data type. Start from 0 index.

  List list_name = [1, 2, 'hifza'];
  print(list_name);
  print(list_name[2]);

  //Map: Data define in key value
  Map map_name = {'name': 'hifza', 'city': 'abbottabad'};
  print(map_name);
  print(map_name['name']);

  //Dynamic

  var dynamic_data = {'name': 'hifza', 'city': 'abbottabad'};
  print(dynamic_data);
  print(dynamic_data['city']);
}
