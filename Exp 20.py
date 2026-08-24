from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing is interesting",
    "Machine learning is useful",
    "Natural language processing uses machine learning"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

for i, score in enumerate(scores):
    print("Document", i + 1, "Score:", round(score, 3))