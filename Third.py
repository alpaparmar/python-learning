# Lists in Python similar to array in javascript

marks = [20, 40, 50, 90, 29]

print(marks)

#list slicing

marks1 = [20, 40, 50, 90, 29]
print(marks1[1:])

# negative indexing with slicikng

marks2 = [20, 40, 50, 90, 29]

print(marks2[-3:])
print(marks2[:-4])

#list methods

marks3 = [20, 40, 50, 90, 29]

marks3.append(100)
print(marks3)
print(marks3.sort())
print(marks3)
print(marks3.reverse())
print(marks3)
print(marks3.pop())
print(marks3)
print(marks3.remove(50))
print(marks3)


# Tuples in Python

# Tuples are immutable

tup = (1, 2, 3, 4, 2, 2, 5)
print(type(tup))

print(tup[1:])

# slicing in tuples

print(tup[-3:])

print(tup.count(2))

# WAP to ask user to enter names of their 3 friends and print and store them in a list

friend1 = input("Enter your friend1 name")

friend2 = input("Enter your friend2 name")

friend3 = input("Enter your friend3 name")

friends = [friend1, friend2, friend3]

print(friends)

# WAP to check list is palindrome or not

palin = [1, 2, 3, 2, 1]
palin1 = palin.copy()

palin1.reverse()

if(palin == palin1):
    print("Palindrome")
else:
    print("Not Palindrome")