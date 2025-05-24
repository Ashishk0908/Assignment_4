# Module 5: Files, Exceptions, and Errors in Python
with open("sample.txt","w") as file:
    file.write("This is a sample text file.\nIt contains multiple lines.")

#print the content
with open("sample.txt","r") as file:
    print("Reading file content:")
    data = file.read()
print(data)

# Print the content line by line
file = open("sample.txt", "r")
print("Reading file content:")
d1 = file.readline() # file.read will read the whole file
print(d1)
d2 = file.readline()
print(d2)
file.close()
#another way
with open("sample.txt","r") as file:
    print("Reading file content:")
    line_no = 1
    for line in file:
        print(line.strip())
        line_no += 1

# if there is no file as sample1
try:
    with open("sample1.txt", "r") as file:
        print("Reading file content:")
        data = file.read()
    print(data)
except FileNotFoundError:
    print("Error: The file 'sample1.txt' was not found.")

# Task 2: Write and Append Data to a File
# enter text to write the file: Hello, Python!
# Data successfully written to output.txt
#
# Enter additional text to append: Learning file handling in python.
# Data successfully appended.
#
# Final content of output.txt
# Hello Python!
# Learning file handling in python.

content = input("Enter text to write the file: ")
with open("output.txt","w") as file:
    file.write(content + "\n")
print("Data successfully written to output.txt")

append_content = input("\nEnter additional text to append: ")
with open("output.txt","a") as file:
    file.write(append_content + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt","r") as file:
    print(file.read())