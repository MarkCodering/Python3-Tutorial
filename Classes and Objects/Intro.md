# Introduction to Object Oriented Programming in Python
## What is Object Oriented Programming (OOP)
### Why modern software use OOP to develop a software?

## How to do OOP in Python?
### Class verus Instance
Here is an sample code in demonstrating the use of class and instance.
```python
class Dog:
     
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def attrFunction(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.attFunction()
```