import re

correo = input("Ingrese el correo: ")

patron = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(patron, correo):
    print("Correo válido")
else:
    print("Correo inválido") 
