//Fibonacci series in JavaScript
//User Input
const num = parseInt(prompt('Enter the number of terms: '));

//Variables
let num1 = 0, num2 = 1, nextNum;

console.log('Fibonacci Series:');

//For loop to Print the series
for (let i = 1; i <= num; i++) {
    console.log(num1);
    nextNum = num1 + num2;
    num1 = num2;
    num2 = nextNum;
}