'''
Author: Jordan (jordanallybrown)
Problem: An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the
number itself.

Algorithm: Start with n as our dividend, then use the remainder of n by dividing by it's base (i.e. base 10) to
isolate each digit. Multiply the remainder by 3 and add it to our total sum (according to Armstrong formula).
Next divide by 10 to move to the next 10's place in the number, and repeat until our dividend has nothing more to
divide it by (i.e. 0) because we've checked all places

Lesson: make use of integer division in python and using the powers of 10 to isolate digits (in base 10)
'''

def getPower1(n):
	'''

	Return the number of places in n

	:param n: positive integer
	:return: int, number of places in the integer, n
	'''
	if n == 0:
		return 1
	else:
		powerCounter = 0
		while n > 0:
			n = n//10
			powerCounter += 1
		return powerCounter

def getPower2(n):
	'''

	Return the number of places in n (simulate a do-while in python)

	:param n: positive integer
	:return: int, number of places in the integer, n
	'''
	powerCounter = 0
	while True:
		n = n//10
		powerCounter += 1
		if n <= 0:
			break
	return powerCounter

def isArmStrongNum(n):
	'''
	Determines whether integer n is an Armstrong number
	:param n: a positive integer
	:return: True if n is an Armstrong number, False otherwise
	'''
	dividend = n
	totalSum = remainder = 0
	power = getPower1(n)
	while dividend > 0:
		remainder = dividend % 10
		totalSum += remainder**power
		dividend = dividend // 10
	return (totalSum == n)


def main():

	print(isArmStrongNum(153)) # True
	print(isArmStrongNum(0)) # True
	print(isArmStrongNum(1)) # True
	print(isArmStrongNum(137)) # False
	print(isArmStrongNum(371)) # True
	print(isArmStrongNum(1634)) # True

main()