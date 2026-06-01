import re
import joblib

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
    "sprintf"
]

SAFE_FUNCTIONS = [
    "fgets",
    "strncpy",
    "snprintf"
]


def has_function(code, function_name):

    pattern = rf"\b{function_name}\s*\("

    return re.search(
        pattern,
        code,
        re.IGNORECASE
    ) is not None


def extract_manual_features(code):

    dangerous_count = sum(
        1
        for func in DANGEROUS
        if has_function(code, func)
    )

    safe_count = sum(
        1
        for func in SAFE_FUNCTIONS
        if has_function(code, func)
    )

    code_length = len(code)

    line_count = len(
        code.splitlines()
    )

    return [
        dangerous_count,
        safe_count,
        code_length,
        line_count
    ]


def predict_code(code):

    dangerous_count = sum(
        1
        for func in DANGEROUS
        if has_function(code, func)
    )

    safe_count = sum(
        1
        for func in SAFE_FUNCTIONS
        if has_function(code, func)
    )

    print(
        f"DEBUG -> dangerous={dangerous_count}, safe={safe_count}"
    )

    if dangerous_count > 0:

        return {
            "result": "VULNERABLE",
            "confidence": 95.0
        }

    if safe_count > 0:

        return {
            "result": "SAFE",
            "confidence": 95.0
        }

    manual_features = csr_matrix([
        extract_manual_features(code)
    ])

    tfidf_features = tfidf.transform(
        [code]
    )

    X = hstack([
        tfidf_features,
        manual_features
    ])

    probs = model.predict_proba(X)[0]

    vulnerable_prob = float(
        probs[1]
    )

    if vulnerable_prob >= 0.95:

        return {
            "result": "VULNERABLE",
            "confidence": round(
                vulnerable_prob * 100,
                2
            )
        }

    return {
        "result": "SAFE",
        "confidence": round(
            (1 - vulnerable_prob) * 100,
            2
        )
    }


if __name__ == "__main__":

    code = """
#include <stdio.h>

int main() {

    char buffer[50];

    fgets(buffer,sizeof(buffer),stdin);

    return 0;
}
"""

    print(
        predict_code(code)
    )