from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
ex_text = "Hello Mr.kit, How are you doing today ? The weather is great and python is awesome... "
words = word_tokenize(ex_text)
filtered_sentence = []
stop_words= set(stopwords.words("english"))
for W in words:
    if W  not in stop_words:
        filtered_sentence .append(W)
print(filtered_sentence)
