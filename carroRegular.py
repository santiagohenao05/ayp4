#Expresión regular para validar si el texto que pasa es la placa de un carro
import re

placa = "ABC123"

if re.match(r'^[A-Z]{3}\s?[0-9]{3}$', placa):
    print("Placa válida")
else:
    print("Placa inválida")