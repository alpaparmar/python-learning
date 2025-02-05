#concetenation of string

first = "Hello Jay "
second = "Welcome to python"

result = first + second

print(result)

# Length of String

findLength = "Hello Jay"
print(len(findLength))


# Slice of String

test = "Hello Jay"
print(test[0:5])
print(test[2: 7])
print(test[:5]) #star index miss
print(test[2:]) #end index miss

#Negative Indexing

test1 = "Hello Jay"
print(test1[-1])
print(test1[-5:-1])
print(test1[-5:])

# Strings Functions

test3 = "Hello Jay Welcome to the Python!!"

print(test3.endswith("Python!!"))
print(test3.startswith("Hello  "))
print(test3.capitalize())
print(test3.replace("Python", "JavaScript"))
print(test3.find("Welcome"))
print(test3.count("l"))

# WAP to input user's first name and print its length

firstI = input("Enter your first name")
print(len(firstI))

# WAP to find Occurence of $ in the given string

OccInput = "Hello Jay $ Welcome to th$ $e Python $$!!"
print(OccInput.count("$"))

#conditional statement

# if, elif, else

userAge = int(input("Enter your age"))

if(userAge >= 18):
    print("You are eligible for voting")
elif(userAge >= 13):
    print("You are a teenager")
else:
    print("You are a kid")


# Nested if

userAge1 = int(input("Enter your age"))

if(userAge1 >= 18):
    if(userAge1 >= 60):
        print("You are a senior citizen")
    else:
        print("You are eligible for voting")
else:
    print("You are a kid")