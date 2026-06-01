import pandas as pd
import numpy as np
import joblib

from scipy.sparse import hstack
from scipy.sparse import csr_matrix

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

from sklearn.linear_model import LogisticRegression

DANGEROUS = [
    "gets",
    "strcpy",
    "strcat",
    "system",
    "exec",
    "eval",
    "scanf",
    "sprintf"
]

SANITIZERS = [
    "snprintf",
    "strncpy",
    "fgets",
    "escape",
    "sanitize"
]


def extract_manual_features(code):

    code = str(code)

    dangerous_count = sum(
        code.count(x)
        for x in DANGEROUS
    )

    sanitizer_count = sum(
        code.count(x)
        for x in SANITIZERS
    )

    code_length = len(code)

    line_count = len(
        code.splitlines()
    )

    return [
        dangerous_count,
        sanitizer_count,
        code_length,
        line_count
    ]


print("Cargando dataset...")

df = pd.read_csv(
    "data/juliet_balanced.csv"
)

print(df["label"].value_counts())

X_text = df["code"].astype(str)

y = df["label"]

print("Extrayendo features manuales...")

manual_features = np.array([
    extract_manual_features(code)
    for code in X_text
])

print("Generando TF-IDF...")

tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    lowercase=True
)

X_tfidf = tfidf.fit_transform(
    X_text
)

X_manual = csr_matrix(
    manual_features
)

X = hstack([
    X_tfidf,
    X_manual
])

print("Dividiendo dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Entrenando Logistic Regression...")

model = LogisticRegression(
    max_iter=3000,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    pred
)

print("\n==========================")
print(f"Accuracy: {accuracy:.4f}")
print("==========================\n")

print(
    classification_report(
        y_test,
        pred
    )
)

joblib.dump(
    {
        "model": model,
        "tfidf": tfidf
    },
    "models/model.joblib"
)

print("Modelo guardado correctamente.")