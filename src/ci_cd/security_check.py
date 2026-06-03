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
from telegram_bot import send_message


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

    send_message(
        f"""
🚨 ALERTA DE SEGURIDAD

Archivo:
{file_path}

Resultado:
{result['result']}

Confianza:
{result['confidence']}%

Vulnerabilidad:
{result.get('vulnerability', 'Desconocida')}

Motivo:
{result.get('reason', 'No disponible')}

Recomendación:
{result.get('recommendation', 'Revisar código')}
"""
    )

    print("Vulnerabilidad detectada")

    sys.exit(1)


send_message(
    f"""
✅ ANÁLISIS COMPLETADO

Archivo:
{file_path}

Resultado:
SAFE

Confianza:
{result['confidence']}%

No se encontraron vulnerabilidades conocidas.
"""
)

print("Código seguro")

sys.exit(0)