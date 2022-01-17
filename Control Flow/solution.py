# Please write a code to calculate the Fibonacci series.
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding numbers.
# The first ten numbers in the Fibonacci series are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

num = input("Enter the length of the series: ")

if num == 0:
    print("0")
elif num == 1:
    print("0, 1")
else:
    print("0, 1", end=", ")
    a = 0
    b = 1
    for i in range(2, int(num)):
        c = a + b
        print(c, end=", ")
        a = b #Iteration
        b = c