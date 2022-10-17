let str = ['Java', 'Python', 'Javascript', 'Django', 'Angular', 'Nodejs'];
let val = prompt('Enter Element name :');

// Using array function
console.log(str.includes(val));

// Using if statement
if (str.includes(val)) {
    console.log(val);
} else {
    console.log('Element not found!!!');
}

// Input : Jav
// Output : false
//          Element not found!!!

// Input : Java
// Output : true
//          Java
