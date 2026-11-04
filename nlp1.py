import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 1. Define your sample text
text = "This is a simple sample sentence showing how to filter stopwords out of a text."

# 2. Tokenize the sentence into individual lowercase words
words = word_tokenize(text.lower())

# 3. Load the standard English stopwords list
stop_words = set(stopwords.words('english'))

# 4. Filter out the stopwords using a list comprehension
filtered_words = [w for w in words if w not in stop_words]

# 5. Print results to see the difference
print("Original Words:\n", words)
print("\nFiltered Words (No Stopwords):\n", filtered_words)
