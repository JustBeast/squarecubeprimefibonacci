# Print factorization (hardest - the meat of the problem)
# def factorize(n):

# Goldbach's conjecture: Return the goldbach pair
# Give two prime numbers that add up to n
# def goldbach(n):

# Twin prime ratio - what percentage of prime numbers are part of a twin prime pair
# def twinPrimeRatio(n)

# Return the largest twin prime pair less than or equal to n
# def largestTwinPrime(n):

# Return the largest prime number that is less than or equal to n
def largestPrime(n):
	while not isPrime(n):
		n = n - 1
	return n

def isPrime(n):
	# If n is 1 or n is even
	if n == 1   or n % 2 == 0:
		return False
	# Fix the n = 2 problem
	if n == 2:
		return True


	for factor in range(2, n):
		if n % factor == 0:
			return False
	return True

def isTwinPrime(n):
	if isPrime(n) and isPrime(n + 2):
		return True
	if isPrime(n) and isPrime(n - 2):
		return True
	return False
def largestTwinPrime(n):
	while not isTwinPrime(n):
		n = n - 1
	return n
	return n - 2
def twinPrimeRatio(n):
	primes = 0
	twinprimes = 0
	while n > 0:
		if isPrime(n):
			primes = primes + 1
		if isTwinPrime(n):
			twinprimes = twinprimes + 1
		n = n - 1
	return twinprimes/primes
def goldbach(n):


for number in range(2, 1000):
	if isPrime(number):
		print(number)
