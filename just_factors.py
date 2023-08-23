from timeit import default_timer as timer
from random import randint
import time
import math

#Finds the first factor of a number by trial division from 2 upto the square root of the number
def factor(num):
	for i in range(2, math.ceil(float(num) ** (1/2)) + 1):
		if (num % i == 0):
			return i

#Runs a certain number of tests on how long it takes to factor a random number between min and max bruh
#and returns the average
def factor_test(tests, n_min, n_max, display):
	if(display):
		print("factoring", tests, "random numbers between", str(n_min), "and", str(n_max))
	start = timer()
	for i in range(0, tests):
		rand = randint(n_min, n_max)
		factor(rand)
	end = timer()
	if(display):
		print("total time:", end-start)
		print("average time:", (end-start)/tests)
	return ((end-start), (end-start)/tests)

def main():
	total, average = factor_test(1000, 1, 1e10, True)

if __name__ == '__main__':
	main()