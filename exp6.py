import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perception_tagger')
sen=input("enter a sentence:")
Words = word_tokenize(sen)
pos_tags=nltk.pos_tag(Words)
print("\nWord\t\tPOS Tag")
print("_ "*15)
for word,tag in pos_tags:
    print(f"{word}\t\t{tag}")