import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required NLTK data models
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Get input text from the user
text = input("Enter a sentence: ")

# Tokenize into words and perform POS tagging
tokens = word_tokenize(text)
tags = pos_tag(tokens)

# Display the results
print("\nPart-of-Speech Tags")
print("-" * 35)
for word, tag in tags:
    print(f"{word:<15} {tag}")
