const sortCharactersInString = str =>
  [...str].sort((a, b) => a.localeCompare(b)).join('');
 
console.log(sortCharactersInString('cabbage'));
