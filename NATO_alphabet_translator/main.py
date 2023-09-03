import pandas

# nato_phonetic_alphabet.csv dataframe
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# use Dictionary comprehension to translate to letter:code format
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# prompt user input
# TEMP BELOW
user_input = "z a b"
    # input("Enter the word you'd like to translate\n"))

# convert user input to to an upper case list for each letter
user_input_list = [letter.upper() for letter in user_input]

# need to pull the code and input it into the phrase

# currently this is going through the nato alphabet and copying over the code if the letter is in the user input
user_phrase_codes_present_list = [code for (letter, code) in nato_dict.items() if letter in user_input_list]

# using for loop need to refactor into a list comprehension
user_phrase = ""
# need to go through the letters in the user input and replace each with the corresponding nato code from the nato_dict
# for letter in user_input_list:
#     if letter == " ":
#         user_phrase += " space"
#     for dict_letter in nato_dict:
#         if letter == dict_letter:
#             user_phrase += f" {nato_dict[dict_letter]}"
# print(user_phrase)

user_phrase_list_comp = [nato_dict[letter] for letter in user_input_list if letter in nato_dict]
print(str.join("", user_phrase_list_comp))

