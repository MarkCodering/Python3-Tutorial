num = input("Enter the length of the series: ")

def fibonacci(num):
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

fibonacci(num)