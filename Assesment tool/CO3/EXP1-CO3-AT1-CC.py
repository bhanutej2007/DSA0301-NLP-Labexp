def parse_cfg(sentence):
    words = sentence.lower().split()

    if len(words) != 5:
        return "Invalid Sentence"

    det1, noun1, verb, det2, noun2 = words

    if det1 not in ["the", "a"]:
        return "Invalid Sentence"

    if noun1 not in ["student", "teacher", "book"]:
        return "Invalid Sentence"

    if verb not in ["reads", "likes"]:
        return "Invalid Sentence"

    if det2 not in ["the", "a"]:
        return "Invalid Sentence"

    if noun2 not in ["student", "teacher", "book"]:
        return "Invalid Sentence"

    parse_tree = (
        "S\n"
        "├── NP\n"
        "│   ├── Det → " + det1 + "\n"
        "│   └── N → " + noun1 + "\n"
        "└── VP\n"
        "    ├── V → " + verb + "\n"
        "    └── NP\n"
        "        ├── Det → " + det2 + "\n"
        "        └── N → " + noun2
    )

    return "Valid Parse Tree\n" + parse_tree


sentence = input("Enter a sentence: ")
print(parse_cfg(sentence))