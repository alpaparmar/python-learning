# File I/o


# Type of file I/O
# 1. Text file: .txt, .csv, .json, .xml, .docx, .xlsx
# 2. Binary file: .jpg, .png, .mp3, .mp4, .pdf


file = open("demo.txt")

# data = file.read()
# print(data)

data = file.read(15)
print(data, "sdd")

data = file.readline()
print(data)

file.close()

# r open file for reading
# w open file for writing
# a open file for appending
# r+ open file for reading and writing
# w+ open file for reading and writing
# a+ open file for reading and writing
# rb open file for reading in binary mode
# wb open file for writing in binary mode
# ab open file for appending in binary mode
# rb+ open file for reading and writing in binary mode
# wb+ open file for reading and writing in binary mode
# x create a new file and open it for writing
# t open file in text mode (default)


#writing to a file

writeData = open("demo.txt", "a")

writeData.write("\n Hello, World new thing!\n I am quick leraning python")

writeData.close()

# file is not exist then it will create a new file

newFile = open("newFile.txt", "w")
newFile.write("Hello, World!")
newFile.close()

# r+ mode will override the content from starting of the file

#with Syntax

with open("demo.txt") as file:
    data = file.read()
    print(data, "Last")


# Delete a file
    
import os

os.remove("newFile.txt")


# Create a new file "practice.txt" and write the following data to it:

data = ["Hi Everyone", "I am learning Python", "I am enjoying", "I will become a Python Developer"]

fileNewData = open("practice.txt", "w")

for i in data:
    fileNewData.write(i + "\n")

fileNewData.close()

file1Data = open("practice.txt", "r+")

data = file1Data.read()
result = data.replace("Python", "JavaScript")

file1Data.write(result)

file1Data.close()