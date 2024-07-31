# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_fram = pandas.DataFrame(nato)
# print(nato_fram)
# for(index, row) in nato_fram.iterrows():
#     print(row.letter, row.code)

new_nato = {row.letter: row.code for (index, row) in nato_fram.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

try:
    user_input = input("Choose a name").upper()
except KeyError:
    print("error")
else:
    list = [new_nato[letter] for letter in user_input]
    print(list)
