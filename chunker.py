import nltk
from nltk.tokenize import word_tokenize
from pprint import pprint

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
VP: {<VB.*><DT>?<JJ>*<NN.*>+}
"""

chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)

print("\nPOS Tagged Sentence")
pprint(tagged_words, width=40)

print("\nChunk Tree\n")
# Formats the string to strip extra internal spacing while preserving parenthetical line breaks
formatted_tree = "\n".join(line.strip() for line in str(chunk_tree).splitlines())
print(formatted_tree)
