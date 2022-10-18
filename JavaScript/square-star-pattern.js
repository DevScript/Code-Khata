// Run two nested for loops to create a square star pattern. Run each loop 'n' times, where 'n' is the number of rows/columns in the square, i.e. for(let i= 0;  i< n; i++).

// The internal loop will run for 'n' times, printing starts in a row and a newline at the end of the loop (n), whereas the outer loop will run the internal loop for 'n' times, printing starts in a column (n).
let n = 5; // row or column count
// defining an empty string
let string = "";

for(let i = 0; i < n; i++) { // external loop
  for(let j = 0; j < n; j++) { // internal loop
    string += "*";
  }
  // newline after each row
  string += "\n";
}
// printing the string
console.log(string);
