import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from ml.predict import predict_code

if len(sys.argv) < 2:
    print("Debe indicar archivo")
    sys.exit(1)

file_path = sys.argv[1]

with open(
    file_path,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    code = f.read()

result = predict_code(code)

print(result)

if result["result"] == "VULNERABLE":
    print("Vulnerabilidad detectada")
    sys.exit(1)

print("Código seguro")
sys.exit(0)