import math
import numpy as np
import unittest
from random import randint

blue = np.loadtxt("blue.csv", dtype=np.uint8, delimiter=",")
red = np.loadtxt("red.csv", dtype=np.uint8, delimiter=",")

def E(data, func= lambda x: math.pow(x,1)):
	count = 0.0
	sum = 0.0
	for val in np.nditer(data):
		sum += func(val)
		count += 1
	return sum/count


def var(data, func= lambda x: math.pow(x,1)):
	mu = E(data)
	expected_sq = E(data, func= lambda x: pow(x,2))
	return (expected_sq - mu**2)

class LinearityTests(unittest.TestCase):

	def test_expected_linearity1(self):

		self.assertFalse(E(blue + red) == E(blue) + E(red))

	def test_expected_linearity2(self):

		random_nums = [randint(2, 100) for i in range(10)]

		for i in random_nums:
			self.assertFalse(E(blue + i) == (E(blue) + i))

	def test_expected_linearity3(self):

		random_nums = [randint(2, 100) for i in range(10)]

		for i in random_nums:
			self.assertFalse(E(i * blue) == (i * E(blue)))

	def test_variance(self):

		a = randint(2, 100)
		b = randint(2, 100)

		left = var(a * red + b)
		right = a * a * var(red)
		self.assertFalse(left == right)


if __name__ == "__main__":

	unittest.main()











