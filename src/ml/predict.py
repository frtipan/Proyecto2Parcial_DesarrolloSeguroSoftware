import joblib
import numpy as np

from scipy.sparse import hstack
from scipy.sparse import csr_matrix

saved = joblib.load(
    "models/model.joblib"
)

model = saved["model"]
tfidf = saved["tfidf"]

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


def predict_code(code):

    tfidf_features = tfidf.transform(
        [code]
    )

    manual_features = csr_matrix([
        extract_manual_features(code)
    ])

    X = hstack([
        tfidf_features,
        manual_features
    ])

    pred = model.predict(X)[0]

    probs = model.predict_proba(X)[0]

    confidence = float(max(probs))

    if pred == 1:
        return {
            "result": "VULNERABLE",
            "confidence": round(
                confidence * 100,
                2
            )
        }

    return {
        "result": "SAFE",
        "confidence": round(
            confidence * 100,
            2
        )
    }


if __name__ == "__main__":

    code = """
#include <stdio.h>

int main() {

    char buffer[10];

    gets(buffer);

    return 0;
}
"""

    result = predict_code(code)

    print(result)