/*
Higher Order Function
Higher order functions are functions which take other function as a parameter or return a function as a value. The function passed as a parameter is called callback.

Callback
A callback is a function which can be passed as parameter to other function. See the example below.
*/

// a callback function, the name of the function could be any name
const callback = (n) => {
  return n ** 2;
};

// function that takes other function as a callback
function cube(callback, n) {
  return callback(n) * n;
}

// console.log(cube(callback, 3)); // can be done without passing callback here. dont understand the purpose of callback here.

// Higher order function returning an other function
const higherOrder = (n) => {
  const doSomething = (m) => {
    const doWhatEver = (t) => {
      return 2 * n + 3 * m + t;
    };
    return doWhatEver;
  };
  return doSomething;
};
// console.log(higherOrder(2)(3)(10));

const numbers = [1, 2, 3, 4, 5];
const arr = [1, 2, 3, 4, 5, 6];
const sum = numbers.reduce((accumulator, currentValue, index, array) => {
  // console.log(`${accumulator} ${currentValue} ${index} ${array}`);
  return accumulator + currentValue;
}, 0);

// console.log(sum);

const names = ["Asabeneh", "Mathias", "Elias", "Brook"];
const areAllStr = names.every((name) => typeof name === "string"); // Are all strings? //same as typeof(name), name.typeofdoesnt.work

// console.log(areAllStr);

const areAllStr1 = names.some((name) => typeof name === "number"); // Are all strings ? // does he mean are some numbers?

// console.log(areAllStr1) // false // no! all are strings.

arr.forEach(function (element, index, arr) {
  // console.log(index, element, arr)
});
// The above code can be written using arrow function
arr.forEach((element, index, arr) => {
  // console.log(index, element, arr)
});
// The above code can be written using arrow function and explicit return

// arr.forEach((element, index, arr) => console.log(index, element, arr))

let sum2 = 0;
const numbers2 = [1, 2, 3, 4, 5];
numbers.forEach((num) => (sum2 += num));

// console.log(sum)

// map
// map: Iterate an array elements and modify the array elements. It takes a callback function with elements, index , array parameter and return a new array.

/*Arrow function and explicit return
const modifiedArray = arr.map((element,index) => element);
*/
//Example
const numbers3 = [1, 2, 3, 4, 5];
const numbersSquare = numbers3.map((num) => num * num);

// console.log(numbersSquare)

/*
***********DIFFERENCE BETWEEN MAP AND FOREACH************

foreach returns a single value, map returns an array.

since map retruns and array, function chaining i.e arr.map(callback(element)).sort().find() can be used in map. but it cant be used in foreach since it returns a single value.


*/

var numbers1 = [1, 5, 3.14];

numbers1.sort((a, b) => a - b);

// console.log(numbers1);

// compare(1,5);     // Returns -4, a is less than b
// compare(1,3.14);  // Return -2.14, a is less than b
// compare(5,3.14);  // returns 1.86, a is greater than b

/*
Going through or short list of three numbers again, you'd start by comparing the first two numbers:

Is 1 greater than or less than 5? Less than, so put these two numbers in our list: 1,5
Is 3.14 greater than or less than 1? Greater than, so it goes after 1 in the new list
Is 3.14 greater than or less than 5 in our new list? Less than, so it goes before 5. Our new list is now [1,3.14,5]
Because you can provide your own compare() function, it is possible to sort arbitrarily complex data, not just numbers.
*/

const users = [
  { name: "Asabeneh", age: 150 },
  { name: "Brook", age: 50 },
  { name: "Eyob", age: 100 },
  { name: "Elias", age: 22 },
];
users.sort((a, b) => {
  if (a.age < b.age) return -1;
  if (a.age > b.age) return 1;
  return 0;
});

/*
OR

users.sort((a, b) => a.age - b.age);
*/

// console.log(users) // sorted ascending
// [{…}, {…}, {…}, {…}]

/* __________________________EXCERSICES_________________ */

const countries2 = ["Finland", "Sweden", "Denmark", "Norway", "IceLand"];
const names0 = ["Asabeneh", "Mathias", "Elias", "Brook"];
const numbers0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const products = [
  { product: "banana", price: 3 },
  { product: "mango", price: 6 },
  { product: "potato", price: "" },
  { product: "avocado", price: 8 },
  { product: "coffee", price: 10 },
  { product: "tea", price: "" },
];

// console.log(typeof products[0].price);

// Use reduce to sum all the numbers in the numbers array.

// console.log(
numbers0.reduce((accumulator, currentValue) => accumulator + currentValue);
// );

// Use reduce to concatenate all the countries2 and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and IceLand are north European countries2

let concatenatedcountries2 = countries2.reduce((accumulator, currentValue) => {
  if (countries2.indexOf(currentValue) == countries2.length - 1) {
    accumulator += ` and ${currentValue} are European countries2`;
  } else {
    accumulator += ", " + currentValue;
  }
  return accumulator;
}, `Estonia`);

// console.log(concatenatedCountries);

// Find the total price of products by chaining two or more array iterators(eg. arr.map(callback).filter(callback).reduce(callback))
let sum1 = 0;
products
  .filter((element) => typeof element.price == "number")
  .forEach((element) => (sum1 += element.price));

// console.log(sum1);
// Find the sum of price of products using only reduce reduce(callback))

sum1 = products.reduce((accumulator, currentValue) => {
  if (typeof currentValue.price == "number") {
    accumulator += currentValue.price;
  }
  return accumulator;
}, 0);

// console.log(sum1);
