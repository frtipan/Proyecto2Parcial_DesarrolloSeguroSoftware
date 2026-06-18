import subprocess

comando = input("Ingrese un comando ")

comandos_permitidos = {
    "fecha": ["date"],
    "directorio": ["ls"]
}

if comando in comandos_permitidos:
    resultado = subprocess.run(
        comandos_permitidos[comando],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)

else:
    print("Comando no permitido")