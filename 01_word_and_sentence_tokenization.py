import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download tokenizer resources (internet required the first time).
nltk.download("punkt")
nltk.download("punkt_tab")

text = "Natural Language Processing is interesting. It helps computers."

words = word_tokenize(text)
print("Word tokens:", words)

sentences = sent_tokenize(text)
print("\nSentence tokens:", sentences)
