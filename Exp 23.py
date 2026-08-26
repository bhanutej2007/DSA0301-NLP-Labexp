from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter text: ")

sentences = [s.strip() for s in text.split(".") if s.strip()]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)

total = 0

for i in range(len(sentences) - 1):
    score = cosine_similarity(vectors[i], vectors[i + 1])[0][0]
    print("Sentence", i + 1, "and", i + 2, ":", round(score, 2))
    total += score

if len(sentences) > 1:
    average = total / (len(sentences) - 1)
    print("Coherence Score:", round(average, 2))

    if average >= 0.3:
        print("Text is reasonably coherent")
    else:
        print("Text has low coherence")