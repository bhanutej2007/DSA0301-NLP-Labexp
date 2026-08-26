import re

text = input("Enter text: ")

sentences = text.split(".")

last_noun = ""

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word.lower() not in ["he", "she", "it", "they", "him", "her", "them"]:
            if word[0].isupper():
                last_noun = word

        if word.lower() in ["he", "she", "it", "they"]:
            if last_noun:
                print(word, "refers to", last_noun)