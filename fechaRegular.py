import re

fecha = input("Ingrese una fecha (dd/mm/yyyy): ")

patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

if re.match(patron, fecha):
    print("Fecha válida")
else:
    print("Fecha inválida")