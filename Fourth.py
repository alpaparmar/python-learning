# Dictionary in Python same as object in JS

dict = {
    "name": "Jay",
    "age": 25
}

print(dict)
print(type(dict))
print(dict["name"])

# Nested Dictionary

dict1 = {
    "name": "Jay",
    "age": 25,
    "education": {
        "school": "St. Xavier",
        "college": "MIT"
    }
}

print(dict1)
print(dict1["education"]["school"])

# Dictionary Methods

dict2 = {
    "name": "Jay",
    "age": 25
}

print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict2.get("name"))
print(dict2.update({"name": "Jayesh"}))
print(dict2.get("name"))

dict2["name"] = "Jay"

print(dict2)


# Set in Python

collection = {1,2,3,4,5,6,7,8,9,10}

print(collection)
print(type(collection))

# removeduplicates

collection1 = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}

print(collection1)

#empty set

collection2 = set()

print(collection2)

# Set Methods

collection3 = {1,2,3,4,5,6,7,8,9,10}

collection3.add(11)
print(collection3)

collection3.remove(11)
print(collection3)

collection3.discard(10)
print(collection3)

collection3.pop()
print(collection3)

collection3.clear()
print(collection3)

# union and intersection

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2))

print(set1.intersection(set2))

value = { ("int", 9), ("float", 9.0) }
print(value)


