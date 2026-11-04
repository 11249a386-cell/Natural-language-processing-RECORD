import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
example_text = "Hello Mr. Smith, how are you doing today?"

stop_words = set(stopwords.words('english'))
words = word_tokenize(example_text)

filtered_sentence = []

for w in words:
    if w.lower() not in stop_words:   # Convert to lowercase for comparison
        filtered_sentence.append(w)

print("Original Tokens:", words)
print("After Removing Stop Words:", filtered_sentence)
