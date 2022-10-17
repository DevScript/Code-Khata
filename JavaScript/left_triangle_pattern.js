To create the left triangle pattern in javascript, run two nested for loops. The external loop will take care of the pattern's columns, while the internal loop will print the pattern's rows.

You can see from the pattern above that we need to run an external loop for 'n' times while the internal loop runs once in the first execution, twice in the second execution, and so on until 'n' times.

let n = 5;
let string = "";
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);
