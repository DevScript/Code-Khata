//LCM of two numbers

// user input
//Make sure input numbers are positive
const num1 = prompt('Enter a first number: ');
const num2 = prompt('Enter a second number: ');

// condition to check minimum
let min = (num1 > num2) ? num1 : num2;

// while loop
while (true) {
    if (min % num1 == 0 && min % num2 == 0) {
        console.log(`The LCM of ${num1} and ${num2} is ${min}`);
        break;
    }
    min++;
}