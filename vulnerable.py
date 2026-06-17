import subprocess

opciones_permitidas = {
    "fecha": ["date"],
    "directorio": ["pwd"]
}

comando = input("Ingrese una opción (fecha/directorio): ")

if comando in opciones_permitidas:
    resultado = subprocess.run(
        opciones_permitidas[comando],
        capture_output=True,
        text=True,
        check=True
    )

    print(resultado.stdout)

else:
    print("Opción no permitida")