import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources (internet required the first time).
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

text = input("Enter text: ")

stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

result = [word for word in words if word.lower() not in stop_words]

print("After removing stop words:", " ".join(result))
