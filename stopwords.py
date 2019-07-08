from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

words = "This is an example showing off stop word filtration"
token = word_tokenize(words)
for word in token:
    if word not in stop_words:
        print(word)