import nltk
from nltk.corpus import words

# Download the English word list (internet required the first time).
nltk.download("words")

dictionary = set(words.words())

text = input("Enter a sentence: ")

for word in text.split():
    if word.lower() in dictionary:
        print(word, "- Correct")
    else:
        print(word, "- Incorrect")
