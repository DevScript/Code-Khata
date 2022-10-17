// To create a right triangle pattern in javascript, you'll need to work with three loops, one external and two internal. The external loop will execute internal loops 'n' times, and the internal loop will create a pattern for each row.
let n = 5;
let string = "";
for (let i = 1; i <= n; i++) {
  // printing spaces
  for (let j = 0; j < n - i; j++) {
    string += " ";
  }
  // printing star
  for (let k = 0; k < i; k++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);
