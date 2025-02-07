# Functions in Python

def greet():
    print("Hello, World!")

greet()
print("Function call ended")

#Calculate the sum of two numbers using a function

def Calculate(a,b):
    return a + b

print(Calculate(10, 20))

#built-in functions

print(abs(-30), "abs")
print(max(10, 20, 30), "max")
print(min(10, 20, 30), "min")
print(pow(2, 3), "pow")
print(round(3.14159), "round")
print(sum([1, 2, 3, 4, 5]), "sum")
print(len([1, 2, 3, 4, 5]), "len")
print(sorted([5, 4, 3, 2, 1]), "sorted")
print(sorted([5, 4, 3, 2, 1], reverse=True), "sorted reverse")


#WAP to find the factorial of a number using a function

def factoria(n):
    if n == 0:
        return 1
    else:
        return n * factoria(n - 1)

print(factoria(5))