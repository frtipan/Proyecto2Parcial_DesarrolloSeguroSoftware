import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from src.ml.predict import predict_code
from backend.notifications.telegram_bot import send_message

# =====================================
# Inicio del análisis
# =====================================

send_message(
    "🔍 Inicio de revisión de seguridad"
)


if len(sys.argv) < 2:

    print("Debe indicar archivo")

    send_message(
        "❌ Error: no se indicó archivo para analizar"
    )

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


# =====================================
# Vulnerabilidad encontrada
# =====================================

if result["result"] == "VULNERABLE":

    send_message(
        f"""
❌ Vulnerabilidad detectada

Archivo:
{file_path}

Resultado:
VULNERABLE

Confianza:
{result['confidence']}%

Vulnerabilidad:
{result.get('vulnerability', 'Desconocida')}

Motivo:
{result.get('reason', 'No disponible')}

Recomendación:
{result.get('recommendation', 'Revisar código')}

PR bloqueado
"""
    )

    print("Vulnerabilidad detectada")

    sys.exit(1)


# =====================================
# Código seguro
# =====================================

send_message(
    f"""
✅ Código seguro

Archivo:
{file_path}

Resultado:
SAFE

Confianza:
{result['confidence']}%

No se encontraron vulnerabilidades conocidas.

Continuando pipeline
"""
)

print("Código seguro")

sys.exit(0)