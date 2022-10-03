# function to merge two sorted arrays
merge <- function(a, b) {
	# create temporary array
	temp <- numeric(length(a) + length(b))

	# take two variables which initially points to
	# starting of the sorted sub arrays
	# and j which points to starting of starting
	# of temporary array
	astart <- 1
	bstart <- 1
	j <- 1
	for(j in 1 : length(temp)) {
		# if a[astart] < b[bstart]
		if((astart <= length(a) &&
			a[astart] < b[bstart]) ||
			bstart > length(b)) {
			# insert a[astart] in temp and increment
			# astart pointer to next
			temp[j] <- a[astart]
			astart <- astart + 1
		}
	else {
			temp[j] <- b[bstart]
			bstart <- bstart + 1		
		}
	}
	temp
}

# function to sort the array
mergeSort <- function(arr) {

	# if length of array is greater than 1,
	# then perform sorting
	if(length(arr) > 1) {
	
		# find mid point through which
		# array need to be divided
		mid <- ceiling(length(arr)/2)
	
		# first part of array will be from 1 to mid
		a <- mergeSort(arr[1:mid])
	
		# second part of array will be
		# from (mid+1) to length(arr)
		b <- mergeSort(arr[(mid+1):length(arr)])
	
		# merge above sorted arrays
		merge(a, b)
	}
# else just return arr with single element
else {
		arr
	}
}

# take sample input
arr <- sample(1:100, 10)

# call mergeSort function
result <- mergeSort(arr)

# print result
result
