// Transpose a matrix (2D array) of numbers (integers or floats) and return the result.
// The matrix is transposed by swapping the rows and columns. The result is a new matrix.
// The original matrix is not changed.
// The input matrix is a 2D array of numbers. The result is a 2D array of numbers.
const transposeMatrix = (matrix) => {
    let result = [];
    for (let i = 0; i < matrix[0].length; i++) { // loop through columns
        result.push([]); // add a new row to the result matrix
    }
    for (let i = 0; i < matrix.length; i++) { // loop through rows of the input matrix
        for (let j = 0; j < matrix[0].length; j++) { // loop through columns of the input matrix
            result[j][i] = matrix[i][j]; // swap rows and columns in the result matrix and add the value to the result matrix
        }
    }
    return result;
}

// Driver to test the transposeMatrix function.
console.log(transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])); // Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
// From
//  [[ 1, 2, 3 ],
//   [ 4, 5, 6 ],
//   [ 7, 8, 9 ]]
// To
// → [[1, 4, 7],
//    [2, 5, 8],
//    [3, 6, 9]]
