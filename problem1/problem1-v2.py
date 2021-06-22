#!/usr/bin/python3.9
# Project Euler

# Using mathematical formulas
# to find multiples of a number

# Inclusion-exclusion principle

# p = number of multiples of a number within a threshold
# p3 = (num - 1)/3

# sum = sum of the multiples of a number within a threshold
# sum3 = (3 * p3 *(p3 + 1)) / 2

# The first two sums account for multiples of 3 and 5,
# the last sum accounts for over-counting multiples of 15
# (which can appear in either of the first two sums)

# Worked perfectly
# Time complexity - Big O notation = O(1)


from math import floor


def sumMultiple35(num):
    p = floor((num - 1)/3)
    sum = (3 * p * (p+1)) // 2

    p = floor((num - 1)/5)
    sum += (5 * p * (p+1)) // 2

    p = floor((num - 1)/15)
    sum -= (15 * p * (p+1)) // 2

    return sum


if __name__ == "__main__":
    print(sumMultiple35(100))
