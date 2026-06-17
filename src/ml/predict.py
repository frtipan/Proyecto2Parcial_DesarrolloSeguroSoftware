def predict_code(code):

    code_lower = str(code).lower()

    # ==========================
    # Reglas seguras Python
    # ==========================

    dangerous_python = [
        "os.system(",
        "eval(",
        "exec(",
        "subprocess.popen(",
        "pickle.loads(",
        "__import__("
    ]

    if not any(x in code_lower for x in dangerous_python):

        simple_safe_patterns = [
            "print(",
            "def ",
            "return ",
            "for ",
            "while ",
            "if ",
            "input(",
            "class "
        ]

        if any(x in code_lower for x in simple_safe_patterns):

            return {
                "result": "SAFE",
                "confidence": 95.0
            }

    # ==========================
    # Reglas vulnerables Python
    # ==========================

    if "os.system(" in code_lower:

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Command Injection",
            "reason": "Uso de os.system()",
            "recommendation": "Utilizar subprocess con lista blanca."
        }

    if "eval(" in code_lower:

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Code Injection",
            "reason": "Uso de eval()",
            "recommendation": "Evitar evaluación dinámica."
        }

    if "exec(" in code_lower:

        return {
            "result": "VULNERABLE",
            "confidence": 99.0,
            "vulnerability": "Code Injection",
            "reason": "Uso de exec()",
            "recommendation": "Evitar ejecución dinámica."
        }

    # ==========================
    # Reglas vulnerables C
    # ==========================

    if any(
        func in code_lower
        for func in SAFE_FUNCTIONS
    ):

        return {
            "result": "SAFE",
            "confidence": 95.0
        }

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

    confidence = float(max(probs))

    if pred == 1:

        info = detect_vulnerability_reason(code)

        return {
            "result": "VULNERABLE",
            "confidence": round(confidence * 100, 2),
            "vulnerability": info["vulnerability"],
            "reason": info["reason"],
            "recommendation": info["recommendation"]
        }

    return {
        "result": "SAFE",
        "confidence": round(confidence * 100, 2)
    }