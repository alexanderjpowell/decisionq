###
### Numerical Algorithms Task 2
### Run on Python2.7
###

import math

# Part A

def find_primes(N):
	if (type(N) != int) or (N <= 0):
		return
	ret = []
	for i in range(2, N + 1):
		if (isPrime(i)):
			ret.append(i)
	return ret

def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# Part B

def Fibonacci_sequence(N):
	if (type(N) != int) or (N <= 0):
		return
	elif N == 1:
		return [1] # or [1, 1] depending on preference
	else:
		ret = [1, 1]
		while True:
			nextNum = ret[-1] + ret[-2]
			if (nextNum <= N):
				ret.append(nextNum)
			else:
				break
		return ret

# Part C

def oddish_numbers(N):
	if (type(N) != int) or (N <= 0):
		return
	ret = []
	count = 11
	while len(ret) < N:
		if (tensDigitIsOdd(count) and relativelyPrime(count, 10)):
			ret.append(count)
		count += 1
	return ret

def tensDigitIsOdd(number):
	num = float(number) / 10.0
	num = int(math.floor(num))
	return num % 2 == 1

def relativelyPrime(a, b):
	while b != 0:
		t = a
		a = b
		b = t % b
	return a == 1



if __name__ == "__main__":

	print "find_primes(20): " + str(find_primes(20))
	print "find_primes(11): " + str(find_primes(11))

	print "Fibonacci_sequence(20): " + str(Fibonacci_sequence(20))
	print "Fibonacci_sequence(21): " + str(Fibonacci_sequence(21))

	print "oddish_numbers(5): " + str(oddish_numbers(5))
	print "oddish_numbers(10): " + str(oddish_numbers(10))












