void main() {
//control structure
  /*if structure
   if-else structure
   if elseif-else structure
   switch case*/

  //if
  var name = 'hifza';

  if (name == 'hifza') {
    print("Your name is Hifza");
  }

  //if else

  if (name == 'hifza') {
    print("Your name is Hifza");
  } else {
    print("Your name is Kanwal");
  }

  // if elseif-else structure

  if (name == 'Developer') {
    print("Your name is developer");
  } else if (name == 'hifza') {
    print("Your name is hifza");
  } else {
    print("Your name is Kanwal");
  }

  //switch

  switch (name) {
    case 'hifza':
      print("Hifza");
      break;

    case 'Developer':
      print("Developer");
      break;

    default:
      print("kanwal");
  }
}
