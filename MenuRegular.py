import re

usuarios = []

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo)

def validar_password(password):

    if len(password) < 8:
        print("La contraseña debe tener mínimo 8 caracteres")
        return False

    if not re.search(r'[A-Z]', password):
        print("Debe tener al menos una letra MAYÚSCULA")
        return False

    if not re.search(r'[a-z]', password):
        print("Debe tener al menos una letra minúscula")
        return False

    if not re.search(r'[0-9]', password):
        print("Debe tener al menos un número")
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Debe tener al menos un carácter especial")
        return False

    return True


def registrar_usuario():

    usuario = input("Ingrese nombre de usuario: ")
    correo = input("Ingrese correo electrónico: ")

    if not validar_correo(correo):
        print("Correo inválido")
        return

    password = input("Ingrese contraseña: ")

    if not validar_password(password):
        print("Contraseña inválida")
        return

    usuarios.append({
        "usuario": usuario,
        "correo": correo,
        "password": password
    })

    print("Usuario registrado correctamente")


def mostrar_usuarios():

    if len(usuarios) == 0:
        print("No hay usuarios registrados")
        return

    print("\nUsuarios registrados:")

    for u in usuarios:
        print("Usuario:", u["usuario"], "| Correo:", u["correo"])


while True:

    print("\n===== MENÚ =====")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()

    elif opcion == "2":
        mostrar_usuarios()

    elif opcion == "3":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")