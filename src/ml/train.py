import pandas as pd
import joblib

from scipy.sparse import hstack
from scipy.sparse import csr_matrix

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


DANGEROUS = [
    "gets",
    "strcpy",
    "strcat",
    "system",
    "exec",
    "eval",
    "scanf",
    "sprintf",
    "os.system",
    "subprocess.popen",
    "pickle.loads"
]

SANITIZERS = [
    "snprintf",
    "strncpy",
    "fgets",
    "strncat",
    "escape",
    "sanitize"
]


def extract_manual_features(code):

    code = str(code).lower()

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

# =====================================
# EJEMPLOS EXTRA PARA C Y PYTHON
# =====================================

extra_examples = pd.DataFrame({

    "code": [

        # C seguros
        """
char buffer[50];
fgets(buffer,sizeof(buffer),stdin);
""",

        """
char destino[50];
strncpy(destino,origen,sizeof(destino));
""",

        """
snprintf(buffer,sizeof(buffer),"%s",cadena);
""",

        # Python seguros
        """
def suma(a,b):
    return a+b

print(suma(2,3))
""",

        """
class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
""",

        # C vulnerables
        """
gets(buffer);
""",

        """
strcpy(destino,origen);
""",

        """
strcat(destino,origen);
""",

        """
sprintf(buffer,"%s",cadena);
""",

        """
system(cmd);
""",

        # Python vulnerables
        """
import os

cmd=input()

os.system(cmd)
""",

        """
eval(user_input)
""",

        """
exec(code)
""",

        """
import subprocess

subprocess.Popen(cmd)
"""
    ],

    "label": [

        0,
        0,
        0,
        0,
        0,

        1,
        1,
        1,
        1,
        1,

        1,
        1,
        1,
        1
    ]

})

df = pd.concat(
    [df, extra_examples],
    ignore_index=True
)

X_text = df["code"]

y = df["label"]

print("Extrayendo features manuales...")

manual_features = [

    extract_manual_features(code)

    for code in X_text

]

manual_features = csr_matrix(
    manual_features
)

print("Generando TF-IDF...")

tfidf = TfidfVectorizer(
    max_features=5000
)

X_tfidf = tfidf.fit_transform(
    X_text
)

X = hstack([
    X_tfidf,
    manual_features
])

print("Dividiendo dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Entrenando LogisticRegression...")

model = LogisticRegression(
    max_iter=3000,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

preds = model.predict(
    X_test
)

acc = accuracy_score(
    y_test,
    preds
)

print("\n====================")
print(f"Accuracy: {acc:.4f}")
print("====================\n")

print(
    classification_report(
        y_test,
        preds
    )
)

joblib.dump(
    {
        "model": model,
        "tfidf": tfidf
    },
    "models/model.joblib"
)

print("Modelo guardado.")