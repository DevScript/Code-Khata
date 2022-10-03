// program to sort words in alphabetical order

// user input
const sentence = prompt('Enter a sentence: ');

// converting sentence to an array
const words = sentence.split(' ');

// sorting the Array
words.sort();

// display the sorted Array of words
console.log('The sorted words are:');

for (const word of words) {
  console.log(word);
}