import re

def validar_telefono(numero):
    """
    Valida números tipo: 3001234567 (10 dígitos que empiezan en 3)
    """
    patron = r'^3\d{9}$'
    return re.match(patron, numero) is not None


# PRUEBA
print(validar_telefono("3001234567"))  # True
print(validar_telefono("1234567890"))  # False

import re

def validar_usuario(usuario):
    """
    Reglas:
    - Solo letras, números y _
    - Entre 4 y 12 caracteres
    """
    patron = r'^\w{4,12}$'
    return re.match(patron, usuario) is not None


# PRUEBA
print(validar_usuario("juan_123"))  # True
print(validar_usuario("a!"))        # False

import re

def extraer_fechas(texto):
    """
    Extrae fechas tipo 12/03/2026 o 12-03-2026
    """
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(patron, texto)


# PRUEBA
print(extraer_fechas("Nos vemos el 12/03/2026 o el 15-04-2025"))

import re

def extraer_fechas(texto):
    """
    Extrae fechas tipo 12/03/2026 o 12-03-2026
    """
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(patron, texto)


# PRUEBA
print(extraer_fechas("Nos vemos el 12/03/2026 o el 15-04-2025"))

import re

def extraer_precios(texto):
    """
    Extrae precios tipo $5000 o $20.000

    Ejemplo:
    "Vale $5000 y también $20.000"
    -> ['$5000', '$20.000']
    """
    patron = r'\$\d+(?:\.\d+)*'
    return re.findall(patron, texto)


# PRUEBA
print(extraer_precios("Vale $5000 y también $20.000"))

import re

def extraer_numeros(texto):
    """
    Extrae todos los números enteros de un texto.

    Ejemplo:
    "Tengo 2 perros y 15 gatos"
    -> ['2', '15']
    """
    patron = r'\d+'
    return re.findall(patron, texto)


# PRUEBA
print(extraer_numeros("Tengo 2 perros y 15 gatos"))