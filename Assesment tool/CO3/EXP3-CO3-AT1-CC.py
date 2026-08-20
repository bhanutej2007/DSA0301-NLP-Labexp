def sentence_probability(sentence):

    words = sentence.lower().split()

    if len(words) != 2:
        return 0.0

    np_prob = {
        "john": 0.6,
        "mary": 0.4
    }

    vp_prob = {
        "runs": 0.5,
        "walks": 0.5
    }

    subject = words[0]
    verb = words[1]

    if subject not in np_prob or verb not in vp_prob:
        return 0.0

    probability = np_prob[subject] * vp_prob[verb]

    return probability


sentence = input("Enter a two-word sentence: ")

print("Sentence Probability:", sentence_probability(sentence))