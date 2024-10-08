import pandas
# creating a dictionary using the csv file
alphabet_dataframe = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dictionary = {row.letter:row.code for (index,row) in alphabet_dataframe.iterrows()}

# creating a list of phonetic code words from a word that the user inputs.
word = input('Enter a word').strip()
word_phonetic  = [alphabet_dictionary[letter.upper()] for letter in word]
# print(word_phonetic)
