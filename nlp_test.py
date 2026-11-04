from nltk.tokenize import word_tokenize,sent_tokenize

# Define your text
my_text = "Natural Language Processing with Python is incredibly fun and useful!"

# Tokenize the text into words
tokens = word_tokenize(my_text)

# Print the tokens
print("Tokenized words:")
print(tokens)
for i in tokens:
    print(i)
