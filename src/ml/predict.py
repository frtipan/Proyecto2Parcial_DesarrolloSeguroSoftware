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

SAFE_FUNCTIONS = [
    "fgets(",
    "strncpy(",
    "snprintf("
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


def detect_vulnerability_reason(code):

    code = str(code).lower()

    if "gets(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "gets() no valida el tamaño del buffer.",
            "recommendation": "Utilizar fgets()."
        }

    if "strcpy(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "strcpy() puede copiar más datos que el tamaño permitido.",
            "recommendation": "Utilizar strncpy()."
        }

    if "strcat(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "strcat() puede sobrescribir memoria.",
            "recommendation": "Utilizar strncat()."
        }

    if "system(" in code:

        return {
            "vulnerability": "Command Injection",
            "reason": "system() ejecuta comandos del sistema operativo.",
            "recommendation": "Validar entradas y evitar system()."
        }

    if "sprintf(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "sprintf() no controla el tamaño del buffer.",
            "recommendation": "Utilizar snprintf()."
        }

    return {
        "vulnerability": "Posible vulnerabilidad",
        "reason": "Detectada por el modelo de Machine Learning.",
        "recommendation": "Revisar manualmente el código."
    }


def predict_code(code):

    code_lower = str(code).lower()

    # Funciones seguras conocidas
    if any(
        func in code_lower
        for func in SAFE_FUNCTIONS
    ):

        return {
            "result": "SAFE",
            "confidence": 95.0
        }

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

    confidence = float(
        max(probs)
    )

    if pred == 1:

        info = detect_vulnerability_reason(
            code
        )

        return {
            "result": "VULNERABLE",
            "confidence": round(
                confidence * 100,
                2
            ),
            "vulnerability": info["vulnerability"],
            "reason": info["reason"],
            "recommendation": info["recommendation"]
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

    char buffer[50];

    fgets(
        buffer,
        sizeof(buffer),
        stdin
    );

    return 0;
}
"""

    print(
        predict_code(code)
    )