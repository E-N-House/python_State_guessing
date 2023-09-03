import pandas

# nato_phonetic_alphabet.csv dataframe
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# use Dictionary comprehension to translate to letter:code format
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# prompt user input
user_input = ("z aa z bb")
    # input("Enter the word you'd like to translate\n"))

# convert user input to to an upper case list for each letter
user_input_list = [letter.upper() for letter in user_input]

print(nato_dict.items())
# need to pull the code and input it into the phrase
# Can I nest these?
user_phrase =[code for (letter, code) in nato_dict.items() if letter in user_input_list]
print("user_input_list")
print(user_input_list)
print("user_phrase")
print(user_phrase)

