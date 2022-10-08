void main() {
  //string functions

  //1. concentanation
  var str1 = 'hifza';
  var str2 = 'kanwal';

  print(str1 + ' ' + str2);

  //2. toLowerCase
  var s1 = 'HifzA';
  print(s1);
  s1 = s1.toLowerCase();
  print(s1);

  //3.toUppweCase
  var v1 = 'kanWal';
  print(v1);
  v1 = v1.toUpperCase();
  print(v1);

  //4. findlength: also count space
  var n1 = 'Hifza ';
  print(n1.length);
  //5. trim: remove starting or ending space
  n1 = n1.trim();
  print(n1.length);

  //6. compare to strings

  /* Compare str1 to str2
  -1 means first string is large, 
  1 means first is small , */
  var st1 = 'Hifza';
  var st2 = 'kanwal';
  print(st1.compareTo(st2));

  //7. replace

  var m1 = 'My name is hifza';
  print(m1.replaceAll('hifza', 'Hifza'));

  //8. split: convert string to array/list (split from where there is a space)

  var sp1 = 'My name is hifza kanwal';

  print(sp1.split(' '));

  //return result in the form of list, such as

  var r = sp1.split(' ');

  print(r[3]);

  //9. need specific character
  var h1 = 'Hi, error My name is Hifza';
  print(h1.substring(10)); //Skip starting 10 characters
  print(h1.substring(4, 10)); // display just 4 to 10 characters
}
