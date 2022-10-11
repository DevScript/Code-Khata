// Appending an object in arrayay with a function

function insertObject(array, obj) {

    // append object by push 
    array.push(obj);
    
    console.log(array);
}

// original array
let array = [0,1,2];

// object to add in array
let object = {
     x: 3,
     y: 12
    };

// running function
insertObject(array, object);
