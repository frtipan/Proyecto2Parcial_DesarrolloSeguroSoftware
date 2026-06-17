import joblib
import re

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
    "sprintf",
    "os.system",
    "subprocess.popen"
]

SANITIZERS = [
    "snprintf",
    "strncpy",
    "strncat",
    "fgets",
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


def detect_vulnerability_reason(code):

    code = str(code).lower()

    if "gets(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de gets().",
            "recommendation": "Utilizar fgets()."
        }

    if "strcpy(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de strcpy().",
            "recommendation": "Utilizar strncpy()."
        }

    if "strcat(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de strcat().",
            "recommendation": "Utilizar strncat()."
        }

    if "sprintf(" in code:

        return {
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de sprintf().",
            "recommendation": "Utilizar snprintf()."
        }

    if "system(" in code or "os.system(" in code:

        return {
            "vulnerability": "Command Injection",
            "reason": "Ejecución insegura de comandos.",
            "recommendation": "Validar entradas."
        }

    if "eval(" in code:

        return {
            "vulnerability": "Code Injection",
            "reason": "Uso de eval().",
            "recommendation": "Evitar eval()."
        }

    if "exec(" in code:

        return {
            "vulnerability": "Code Injection",
            "reason": "Uso de exec().",
            "recommendation": "Evitar exec()."
        }

    return {
        "vulnerability": "Posible vulnerabilidad",
        "reason": "Detectada por el modelo ML.",
        "recommendation": "Revisar manualmente."
    }

def predict_code(code):

    code_lower = str(code).lower()

    # =====================================
    # VULNERABILIDADES PYTHON
    # =====================================

    if re.search(r"\bos\.system\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Command Injection",
            "reason": "Uso de os.system().",
            "recommendation": "Utilizar subprocess seguro."
        }

    if re.search(r"\beval\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Code Injection",
            "reason": "Uso de eval().",
            "recommendation": "Evitar eval()."
        }

    if re.search(r"\bexec\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Code Injection",
            "reason": "Uso de exec().",
            "recommendation": "Evitar exec()."
        }

    # =====================================
    # VULNERABILIDADES C
    # =====================================

    if re.search(r"\bgets\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de gets().",
            "recommendation": "Utilizar fgets()."
        }

    if re.search(r"\bstrcpy\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de strcpy().",
            "recommendation": "Utilizar strncpy()."
        }

    if re.search(r"\bstrcat\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de strcat().",
            "recommendation": "Utilizar strncat()."
        }

    if re.search(r"\bsprintf\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Buffer Overflow",
            "reason": "Uso de sprintf().",
            "recommendation": "Utilizar snprintf()."
        }

    if re.search(r"\bsystem\s*\(", code_lower):

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Command Injection",
            "reason": "Uso de system().",
            "recommendation": "Validar entradas."
        }

    # =====================================
    # CÓDIGO SEGURO C
    # =====================================

    if (
        re.search(r"\bfgets\s*\(", code_lower)
        or re.search(r"\bstrncpy\s*\(", code_lower)
        or re.search(r"\bsnprintf\s*\(", code_lower)
        or re.search(r"\bstrncat\s*\(", code_lower)
    ):

        return {
            "result": "SAFE",
            "confidence": 95.0
        }

    # =====================================
    # CÓDIGO SEGURO PYTHON
    # =====================================

    if (
        "def " in code_lower
        or "class " in code_lower
        or "print(" in code_lower
        or "return " in code_lower
    ):

        return {
            "result": "SAFE",
            "confidence": 95.0
        }

    # =====================================
    # MODELO ML
    # =====================================

    tfidf_features = tfidf.transform([code])

    manual_features = csr_matrix([
        extract_manual_features(code)
    ])

    X = hstack([
        tfidf_features,
        manual_features
    ])

    pred = model.predict(X)[0]

    probs = model.predict_proba(X)[0]

    confidence = round(
        float(max(probs)) * 100,
        2
    )

    if pred == 1:

        info = detect_vulnerability_reason(code)

        return {
            "result": "VULNERABLE",
            "confidence": confidence,
            "vulnerability": info["vulnerability"],
            "reason": info["reason"],
            "recommendation": info["recommendation"]
        }

    return {
        "result": "SAFE",
        "confidence": confidence
    }