#!/usr/bin/python3.9
# Project Euler
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23. Find the sum of all the multiples
# of 3 or 5 below N.

# Using Comprehension
# Exceeded time limit in hackerrank for two test cases
# Time complexity - Big O notation = O(n²)

def sumMultiple35(num):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(sumMultiple35(1000))
