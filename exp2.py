from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
ex_txt="Hello Mr.smith,How are you doing today? The weather is great and python is awesome..."
print(word_tokenize(ex_txt))
print(sent_tokenize (ex_txt))
for i in word_tokenize(ex_txt):
    print(i)