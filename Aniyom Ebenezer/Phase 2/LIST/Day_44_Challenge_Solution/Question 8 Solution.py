"""
Write a Python program to replace last element in a list with another list.
"""
num1 = [1, 3, 5, 7, 9]
num2 = [2, 4, 6, 8, 0]
num1[-1:] = num2
print(num1)