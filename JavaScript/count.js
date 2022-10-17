function vowel_count(str) {

  return str.match(/[aeiou]/gi).length;

}

console.log(vowel_count('The quick brown fox jumps over the lazy dog'));
