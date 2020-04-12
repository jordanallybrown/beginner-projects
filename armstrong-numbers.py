'''
Author: Jordan (jordanallybrown)
Problem: An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the
number itself.

Lesson: make use of integer division in python and using the powers of 10 to isolate digits (in base 10)
'''


def isArmStrongNum(n):
	'''
	Determines whether integer n is an Armstrong number

	Algorithm: Start with n as our dividend, then use the remainder of n by dividing by it's base (i.e. base 10) to
	isolate each digit. Multiply the remainder by 3 and add it to our total sum (according to Armstrong formula).
	Next divide by 10 to move to the next 10's place in the number, and repeat until our dividend has nothing more to
	divide it by (i.e. 0) because we've checked all places
	:param n: a positive integer
	:return: True if n is an Armstrong number, False otherwise
	'''
	dividend = n
	totalSum = remainder = 0
	while dividend > 0:
		remainder = dividend % 10
		totalSum += remainder**3
		dividend = dividend // 10
	return (totalSum == n)

def main():

	print(isArmStrongNum(153)) # True
	print(isArmStrongNum(0)) # True
	print(isArmStrongNum(1)) # True
	print(isArmStrongNum(137)) # False
	print(isArmStrongNum(371)) # True

main()