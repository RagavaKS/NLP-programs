import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Download tokenizer resources (internet required the first time).
nltk.download("punkt")
nltk.download("punkt_tab")

text = input("Enter a text: ")

words = word_tokenize(text.lower())
freq = FreqDist(words)

print("Word Frequency:")

for word, count in freq.items():
    print(word, ":", count)
