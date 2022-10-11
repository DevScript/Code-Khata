//Remove duplicate Items from an array

function getUnique(array){
    
    let uniqueArr = [];
    
    // loop through array
    for(let i of array) {
        if(uniqueArr.indexOf(i) === -1) {
            uniqueArr.push(i);
        }
    }
    console.log(uniqueArr);
}

const array = [1, 2, 3, 1, 3];

//Running the function
getUnique(array);