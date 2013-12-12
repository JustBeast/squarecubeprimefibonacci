squarecubeprimefibonacci

========================

def isPerfectSquare(n):
	for x in range(1, n):
		if x**2 == n:
			return True
		if x**2 > n:
			return False 
	return False

	 

def isPerfectCube(n):
	for x in range(1, n):
		if x**3 == n:
			return True
		if x**3 > n:
			return False
		return False 
			


def isPrime(n):
	for x in range (2, n/2 + 1):
		if n%x == 0:
			return False
	return True 

	#

for n in range(100):

	print fibonacci(n)

def fibonacci(n):
	pos=1
	ret=1
	while True:
		if n == pos:
			return ret
		else:
			pos= pos +1
			ret = pos 

		 x#(the fibonacci number for example 1,1,2,3,5,8,13)
		x=x+y
		y=x-y 







	
