def check_agreement(subject, verb):

    subjects = {
        "he": "singular",
        "she": "singular",
        "it": "singular",
        "they": "plural"
    }

    verbs = {
        "runs": "singular",
        "writes": "singular",
        "run": "plural",
        "write": "plural"
    }

    if subject not in subjects or verb not in verbs:
        return False

    return subjects[subject] == verbs[verb]


subject = input("Enter subject: ").lower()
verb = input("Enter verb: ").lower()

if check_agreement(subject, verb):
    print("Agreement is correct")
else:
    print("Agreement is incorrect")