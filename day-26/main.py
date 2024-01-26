
from pandas import read_csv

# accept users name 

name = input("enter your name").upper()

letters_in_name = [letter for letter in name]

data = read_csv("nato_phonetic_alphabet.csv")
codes = data["code"].tolist()
all_letters = data["letter"].tolist()

# finding dictionary for of csv file

dict_form = {all_letters[i]: codes[i] for i in range(26)}

# creating alphaphonetic words


letter_word_join = [dict_form[letter] for letter in letters_in_name ]

print(letter_word_join)


