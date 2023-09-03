import pandas

# nato_phonetic_alphabet.csv dataframe
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# use Dictionary comprehension to translate to letter:code format
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.

# prompt user input AND
# convert user input to an upper case
user_input = input("Enter the word you'd like to translate\n").upper()

# need to pull the code and input it into the phrase

# refactored above into list comprehension this skips over letters or symbols not in nato_dict
code_phrase = [f"{nato_dict[letter]} " if letter in nato_dict else "space " if letter == " " \
    else letter for letter in user_input]
print(str.join("", code_phrase))


# OLDER CODE
# currently this is going through the nato alphabet and copying over the code if the letter is in the user input
# user_phrase_codes_present_list = [code for (letter, code) in nato_dict.items() if letter in user_input]

# using for loop need to refactor into a list comprehension
# user_phrase = ""
# need to go through the letters in the user input and replace each with the corresponding nato code from the nato_dict
# for letter in user_input_list:
#     if letter == " ":
#         user_phrase += " space"
#     for dict_letter in nato_dict:
#         if letter == dict_letter:
#             user_phrase += f" {nato_dict[dict_letter]}"
# print(user_phrase)


