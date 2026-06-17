# safe_example.py

def saludar(nombre):
    return f"Hola {nombre}"

def suma(a, b):
    return a + b

if __name__ == "__main__":
    usuario = input("Ingrese su nombre: ")
    print(saludar(usuario))
    print("Resultado:", suma(10, 20))