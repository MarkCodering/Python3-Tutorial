# Introduction to Python Control Flow
There are two main control flows in programming, which are:
- Conditional Statements
- Looping Statements

## Python Conditional Statements
Conditional statements are used to perform different actions based on different conditions.
```python
x = 10
if x>5:
    print("x is greater than 5")
else:
    print("x is less than 5")
```

Also, you could add multiple conditions to a single conditional statement.
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Python Looping Statements
Looping statements are used to repeat a block of code for a specified number of times.
#### While loop
```python
# While loop
i = 1
while i<=5:
    print(i)
    i += 1
```
#### For loop
```python
# For loop
for i in range(1,6):
    print(i)
```

