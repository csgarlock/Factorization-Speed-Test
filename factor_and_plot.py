from timeit import default_timer as timer
from random import randint
import time
import math
import numpy as np
import matplotlib.pyplot as plt

#Finds the first factor of a number by trial division from 2 upto the square root of the number
def factor(num):
	for i in range(2, math.ceil(float(num) ** (1/2)) + 1):
		if (num % i == 0):
			return i

#Runs a certain number of tests on how long it takes to factor a random number between min and max
#and returns the average
def factor_test(tests, min, max):
	start = timer()
	for i in range(0, tests):
		rand = randint(min, max)
		factor(rand)
	end = timer()
	return ((end-start), (end-start)/tests)

#Generates the axis to be used by matplotlib. Takes evenly spaced samples between n_max
#and n_min. Then runs a factor test for each for the samples
def gen_axis(samples, n_min, n_max, factor_samples):
	x_axis = np.linspace(n_min, n_max, samples)
	y_axis_list = []
	for i in x_axis:
		y_axis_list.append(factor_test(factor_samples, 1, math.ceil(i))[1])
	y_axis = np.array(y_axis_list)
	return (x_axis, y_axis)

def main():
	total, average = factor_test(1000, 1, 1e7)
	print(total)
	print(average)
	# max = 100000000
	# x_fac, y_fac = gen_axis(250, 1, max, 30000)
	# fig, ax = plt.subplots()
	# ax.set_xlabel("Size of Maximum Integer")
	# ax.set_ylabel("Time in Seconds")
	# ax.plot(x_fac, y_fac)
	# fig.show()
	# plt.show()

if __name__ == '__main__':
	main()