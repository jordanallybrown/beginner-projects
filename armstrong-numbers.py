'''
Author: Jordan (jordanallybrown)
Problem: An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the
number itself.

Lesson: make use of integer division in python and using the powers of 10 to isolate digits (in base 10)
'''


def isArmStrongNum(n):
	'''
	Determines whether integer n is an Armstrong number
	:param n: a positive integer
	:return: True if n is an Armstrong number, False otherwise
	'''
	dividend = n
	totalSum = remainder = 0
	while dividend > 0: # stop once our dividend has nothing more to divide it by, we've checked all places of n
		remainder = dividend % 10 # use the remainder of n by dividing by it's base (i.e.10) to isolate each digit
		totalSum += remainder**3
		dividend = dividend // 10 # divide by 10 to move to next digit/10s place in number, and so on
	return (totalSum == n)

def main():

	print(isArmStrongNum(153)) # True
	print(isArmStrongNum(0)) # True
	print(isArmStrongNum(1)) # True
	print(isArmStrongNum(137)) # False
	print(isArmStrongNum(371)) # True

main()