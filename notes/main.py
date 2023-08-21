# file = open("my_file.txt")
# contents = file.read()
#
# print(file)
# print(contents)


# don't forget to close to keep memory space going
# file.close()

# this will open and then close when finished but is in read only default mode
with open("my_file.txt") as file_var:
    contents = file_var.read()
    print(contents)

# this will allow you to write OVER a file but won't let you then print it out
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")

# this will allow you to append or add more text without deleting a file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew New Text.")

with open("new_file.txt", mode="w") as new_file:
    new_file.write("The file didn't exist at first and we are in write mode.\n so the computer created the new_file.txt and then added this info")