prime=''
count=0
i=2
while count!=10:
	for j in range(2,i):
		if i%j==0:
			prime='not prime'
			break
	if prime:
		i=i+1
		prime=''
	else:
		print("{} prime".format(i))
		i=i+1
		count=count+1
