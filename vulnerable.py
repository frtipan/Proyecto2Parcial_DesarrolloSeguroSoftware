import os
import sqlite3
import subprocess

def login():
    username = input("Usuario: ")
    password = input("Password: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login correcto")

        # Command Injection
        cmd = input("Ingrese comando: ")
        os.system(cmd)

        # Dangerous eval
        code = input("Ingrese código Python: ")
        eval(code)

    else:
        print("Credenciales incorrectas")

    conn.close()


def backup():
    file_name = input("Archivo: ")

    # Command Injection
    subprocess.call("cp " + file_name + " backup/", shell=True)


def read_config():
    path = input("Ruta configuración: ")

    with open(path, "r") as f:
        print(f.read())


if __name__ == "__main__":
    login()
    backup()
    read_config()