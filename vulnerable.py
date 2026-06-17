import os

def ejecutar_comando():

    comando = input(
        "Ingrese un comando: "
    )

    os.system(
        comando
    )


if __name__ == "__main__":

    ejecutar_comando()
