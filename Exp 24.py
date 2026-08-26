def dialog_act(sentence):

    text = sentence.lower()

    if any(x in text for x in ["hello", "hi", "hey"]):
        return "Greeting"

    elif "?" in text:
        return "Question"

    elif any(x in text for x in ["please", "can you", "could you"]):
        return "Request"

    elif any(x in text for x in ["thank you", "thanks"]):
        return "Thanks"

    elif any(x in text for x in ["bye", "goodbye"]):
        return "Goodbye"

    elif any(x in text for x in ["yes", "sure", "okay"]):
        return "Answer"

    else:
        return "Statement"


text = input("Enter dialog: ")

for sentence in text.split("."):
    if sentence.strip():
        print(sentence.strip(), "->", dialog_act(sentence))