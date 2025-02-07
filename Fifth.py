#Loops in Python

#While loop

count = 0

while count < 10:
    print(count)
    count += 1


loopData = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

x = 7
i = 0

while i < len(loopData):
    if loopData[i] == x:
        print("Element found at index: ", i)
        break
    i += 1


#For loop

listData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in listData:
    print(i, "For Loop")


# for loop with optional else block
    
for i in listData:
    print(i, "For Loop=====>")
else:
    print("Loop completed successfully")


# search for a number in a list using for loop:

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in data:
    if i == 7:
        print("Element found at index", i)
        break


# range() function
    
for i in range(10):
    print(i, "Range Function")

for i in range(1, 10):
    print(i, "Range Function ->")

for i in range(1, 10, 2):
    print(i, "Range Function - ->")


# Pass statement
    
for i in range(10):
    pass
print("Pass statement executed successfully")


# WAP to find the sum of first n natural numbers using while loop

dataInp = int(input("Enter the number: "))

sum = 0

result = 1

while sum <= dataInp:
    result += sum
    sum += 1

print("Sum of first", dataInp, "natural numbers is: ", result)


# WAP to find the factorial of a number using for loop

dataInp = int(input("Enter the number: "))

result1 = 1
for i in range(4, 1, -1):
    result1 *= i

print("Factorial of", dataInp, "is: ", result1)