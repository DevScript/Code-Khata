// Function to merge two sorted (increasing) arrays of numbers

function mergeTwoSortedArrays(arr1, arr2) {
	// Setup pointers (indexes for traversing arrays), and mergedArray array
	let ptr1 = 0
	let ptr2 = 0
	let mergedArray = []

	// Check for empty input
	if (arr1.length === 0 && arr2.length === 0) return mergedArray // if both arrays empty return empty mergedArray
	if (arr1.length === 0) return arr2 // if arr1 is empty return arr2
	if (arr2.length === 0) return arr1 // if arr2 is empty return arr1

	// While either pointer is not equal to length of their array:
	while (ptr1 < arr1.length && ptr2 < arr2.length) {
		// Add arr1[ptr1] to mergedArray array and increase ptr1 by 1
		if (arr1[ptr1] <= arr2[ptr2]) {
			mergedArray.push(arr1[ptr1])
			ptr1++
		}
		// Add arr2[ptr2] to mergedArray array and increase ptr2 by 1
		else if (arr1[ptr1] > arr2[ptr2]) {
			mergedArray.push(arr2[ptr2])
			ptr2++
		}
	}

	// If ptr1 hasn't traversed all of arr1, push these remaining arr1 values to mergedArray
	while (ptr1 < arr1.length) {
		mergedArray.push(arr1[ptr1])
		ptr1++
	}
	// If ptr2 hasn't traversed all of arr2, push these remaining arr2 values to mergedArray
	while (ptr2 < arr2.length) {
		mergedArray.push(arr2[ptr2])
		ptr2++
	}

	return mergedArray
}

// Driver code to test above
const array1 = [0, 3, 4, 31]
const array2 = [4, 6, 30]
console.log(mergeTwoSortedArrays(array1, array2)) // [0, 3, 4, 4, 6, 30, 31]
