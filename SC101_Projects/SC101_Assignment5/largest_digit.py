"""
File: largest_digit.py
Name: Max Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9
	print(digit_sum(1729))
	print(digits_sorted(-2345))


def find_largest_digit(n):
	"""
	:param n: int entered to find the largest.
	:return: Largest digit of entered int.
	"""
	largest = 0
	return find_largest_digit_helper(n, largest)


def find_largest_digit_helper(n, largest):
	# Make n always bigger than 0
	if n < 0:
		n *= -1
	# If n is a single digit, base case!
	if n < 10:
		if n > largest:
			largest = n
		return largest
	# If n bigger than 10, use mod to compare last digit with largest
	elif n % 10 > largest:
		largest = n % 10
	# Use floor division with 10 to do recursion
	return find_largest_digit_helper(n // 10, largest)


def digit_sum(num):
	# Your Code Here
	total = 0
	if num < 0:
		return -(digit_sum_helper(num, total))
	return digit_sum_helper(num, total)


def digit_sum_helper(num, total):
	if num < 0:
		num *= -1
	if num < 1:
		return total
	else:
		total += num % 10
	return digit_sum_helper(num // 10, total)


def digits_sorted(num: int) -> bool:
	# Your Code Here
	if num < 0:
		num *= -1
	if num < 10:
		return True
	else:
		if num % 10 < (num // 10) % 10:
			return False
		return digits_sorted(num // 10)


if __name__ == '__main__':
	main()
