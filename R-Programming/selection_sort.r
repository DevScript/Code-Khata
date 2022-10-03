# function to sort array using selection sort
selection_sort <- function(x)
{
	# length of array
	n <- length(x)
	for (i in 1 : (n - 1))
	{
		# assume element at i is minimum
		min_index <- i
		for (j in (i + 1) : (n))
		{
			# check if element at j is smaller
			# than element at min_index
			if (x[j] < x[min_index]) {
				# if yes, update min_index
				min_index = j
			}
		}
		# swap element at i with element at min_index
		temp <- x[i]
		x[i] <- x[min_index]
		x[min_index] <- temp
	}
	x
}

# take sample input
arr <- sample(1 : 100, 10)

# sort array
sorted_arr <- selection_sort(arr)

# print array
sorted_arr
