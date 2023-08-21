PLACEHOLDER = "[name]"
# Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as sample_letter:
    sample_letter_content = sample_letter.read()
    # print(sample_letter_content)

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    names_content = names.read()
    # Alt method
    # names_list_alt = names.readlines()
    # returns a name\n list
    names_list = names_content.split("\n")

# Replace the [name] placeholder with name from list.
for curr_name in names_list:
    new_letter = sample_letter_content.replace(PLACEHOLDER, curr_name)
    # name final files to letter_for_NAME
    file_name = f"letter_for_{curr_name}.txt"
    # Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/{file_name}", mode="w") as curr_letter:
        curr_letter.write(new_letter)




# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp