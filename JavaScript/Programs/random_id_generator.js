//charcodes
let a = 97;
let z = 122;

let A = 65;
let Z = 90;

let smallABC = []
let bigABC = []
let nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for (let i = a; i <= z; i++) {
    let alphabet = String.fromCharCode(i);
    smallABC.push(alphabet);
}

for (let i = A; i <= Z; i++) {
    let alphabet = String.fromCharCode(i);
    bigABC.push(alphabet);
}


function randomIDGenerator(n) {
    let randomId = '';
    let characters = smallABC.concat(bigABC);
    characters = characters.concat(nums).toString();
    characters = characters.replaceAll(',', ''); //removing commas
    console.log(characters);
    for (let i = 0; i < n; i++) {
        let randomIndex = Math.floor(Math.random() * characters.length);
        randomId += characters.charAt(randomIndex);
    }

    return randomId;
}

console.log(randomIDGenerator(3))

//PS: this is not so good & not so random id generator as it might generate some duplicate patterns, so you have to add extra conditions for 
//checking the duplicacy.

//Another solution is to use uuid package to generate random keys, it can be installed thru npm.