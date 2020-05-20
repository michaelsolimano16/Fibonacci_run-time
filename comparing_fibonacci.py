# Michael Solimano 2020
# Comparing fibonacci sequence methods for speed (recursion vs memoization)

def fib_recursion(nth_val):
	#use recursion to solve nth val of fibonacci sequence

	if nth_val == 1:
		return 1
	elif nth_val == 0:
		return 0
	else:
		return fib_recursion(nth_val - 1) + fib_recursion(nth_val - 2)

def fib_memoization(nth_val):
	#Fill a list as we go to quickly find previous fib values.
	#This reduces the reduntant calls from the recursive method.

	fibs = [None]*nth_val
	fibs[0] = 1
	fibs[1] = 1

	#fill the array from two to nth value
	counter = 2
	while counter < nth_val:
		fibs[counter] = fibs[counter-1] + fibs[counter-2]
		counter += 1

	#The last value in the array is the desired fib value
	return fibs[-1]


fifth = fib_recursion(5)
print(fifth)

sixth = fib_memoization(6)
print(sixth)

