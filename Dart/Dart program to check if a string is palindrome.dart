import 'dart:io';

void main() {
  print('Enter Any String ');
  String name = stdin.readLineSync()!;

  var sb = StringBuffer();

  for (int i = name.length - 1; i >= 0; i--) {
    sb.write(name[i]);
  }

  if (name == sb.toString()) {
    print('right');
  }
}
