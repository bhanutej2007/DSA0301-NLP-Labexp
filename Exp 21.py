import spacy
from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_sm")

text = input("Enter sentence: ")

doc = nlp(text)

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)

    word = chunk.root.text
    synsets = wordnet.synsets(word)

    if synsets:
        print("Meaning:", synsets[0].definition())
    else:
        print("Meaning: Not found")

    print()