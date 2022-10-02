//Insertion sort lgorithms

function insertionSort2(arr) {

	//we don't need to start at index 0, since by itself, it is already sorted.
	for (let i = 1; i < arr.length; i++)
	{
		//This is the element we are inserting to the correct location
		let key = arr[i];

		//Start checking against all elements on the left, until the beginning of array
		//Or until it found an element that is smaller than the key.
		let j = i - 1;
		while (j >= 0 && arr[j] > key) 
		{
			//Move the element one step to the right
			arr[j + 1] = arr[j];
			j = j - 1
		}

		//insert the key into the correct location
		arr[j + 1] = key;
	}

	return arr;
} 