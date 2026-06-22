import os


class Sistema:

    def __init__(self):

        self.usuario = "admin"

    def mostrar_menu(self):

        print("==============")
        print(" SISTEMA ")
        print("==============")
        print("1. Ejecutar comando")
        print("2. Salir")

    def ejecutar(self):

        comando = input(
            "Ingrese un comando del sistema: "
        )

        os.system(
            comando
        )


def main():

    sistema = Sistema()

    sistema.mostrar_menu()

    opcion = input(
        "Seleccione una opción: "
    )

    if opcion == "1":

        sistema.ejecutar()

    elif opcion == "2":

        print(
            "Saliendo..."
        )

    else:

        print(
            "Opción inválida"
        )


if __name__ == "__main__":

    main()