import re

DANGEROUS_FUNCTIONS = [
    "eval",
    "exec",
    "os.system",
    "subprocess",
    "system(",
    "Runtime.getRuntime",
    "SELECT",
    "INSERT",
    "DELETE",
    "UPDATE"
]

SANITIZERS = [
    "escape",
    "sanitize",
    "html.escape",
    "preparedStatement"
]


def extract_features(code):

    code = str(code)

    dangerous_count = 0

    for func in DANGEROUS_FUNCTIONS:
        dangerous_count += code.count(func)

    sanitizer_count = 0

    for san in SANITIZERS:
        sanitizer_count += code.count(san)

    length = len(code)

    num_lines = len(code.splitlines())

    return [
        dangerous_count,
        sanitizer_count,
        length,
        num_lines
    ]