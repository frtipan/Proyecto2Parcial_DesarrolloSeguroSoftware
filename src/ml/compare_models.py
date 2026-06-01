import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("data/juliet_balanced.csv")

X = df["code"].astype(str)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2)
)

X_train = tfidf.fit_transform(X_train)
X_test = tfidf.transform(X_test)

models = {
    "RandomForest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "SVM": LinearSVC(),

    "LogisticRegression": LogisticRegression(
        max_iter=2000
    ),

    "NaiveBayes": MultinomialNB()
}

for name, model in models.items():

    print(f"\nEntrenando {name}...")

    model.fit(
        X_train,
        y_train
    )

    pred = model.predict(
        X_test
    )

    acc = accuracy_score(
        y_test,
        pred
    )

    print(
        f"{name}: {acc:.4f}"
    )