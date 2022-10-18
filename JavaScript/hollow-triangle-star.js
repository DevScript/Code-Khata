// To make a hollow triangle star pattern, follow these steps:
// Run two nested loops, the first for 'n' times and the second for one time for the first row, the second for two times for the second row, and so on until 'n' times.
// Print a star for the first and last positions in each row, as well as a space for other positions.
// In the final line, print a star in each position.
// Example

let n = 6;
let string = "";

for (let i = 1; i <= n; i++) {
  // printing star
  for (let j = 0; j < i; j++) {
    if(i === n) {
      string += "*";
    }
    else {
      if (j == 0 || j == i - 1) {
        string += "*";
      }
      else {
        string += " ";
      }
    }
  }
  string += "\n";
}
console.log(string);
