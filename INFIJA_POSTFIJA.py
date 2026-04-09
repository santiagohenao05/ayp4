"""
Conversión de expresión INFija a POSTfija (Notación Polaca Inversa)

Ejemplo:
Infija:  A + B * C
Postfija: A B C * +

Se usa una pila para operadores.
"""

# 🔹 Función para prioridad de operadores
def prioridad(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infija_a_postfija(expresion):
    pila = []
    salida = []

    for caracter in expresion:
        
        # Si es operando (letras o números)
        if caracter.isalnum():
            salida.append(caracter)

        # Si es paréntesis de apertura
        elif caracter == '(':
            pila.append(caracter)

        # Si es paréntesis de cierre
        elif caracter == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # quitar '('

        # Si es operador
        else:
            while (pila and prioridad(caracter) <= prioridad(pila[-1])):
                salida.append(pila.pop())
            pila.append(caracter)

    # Vaciar pila
    while pila:
        salida.append(pila.pop())

    return " ".join(salida)


# 🔥 PRUEBAS
print(infija_a_postfija("A+B*C"))      # A B C * +
print(infija_a_postfija("(A+B)*C"))    # A B + C *
print(infija_a_postfija("A+B*C-D"))    # A B C * + D -

"""
Evaluar una expresión en notación postfija usando una pila.

Ejemplo:
Postfija: "2 3 4 * +"
Resultado: 2 + (3 * 4) = 14
"""

def evaluar_postfija(expresion):
    pila = []

    for token in expresion.split():
        
        # Si es número, lo metemos a la pila
        if token.isdigit():
            pila.append(int(token))
        
        else:
            # Sacamos los dos últimos números
            b = pila.pop()
            a = pila.pop()

            # Aplicamos operación
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)

    return pila[0]


# 🔥 PRUEBAS
print(evaluar_postfija("2 3 +"))        # 5
print(evaluar_postfija("2 3 4 * +"))    # 14
print(evaluar_postfija("5 1 2 + 4 * + 3 -"))  # 14

"""
Programa completo:
1. Convierte una expresión INFija a POSTfija
2. Evalúa la expresión POSTfija

Ejemplo:
Infija:  2+3*4
Postfija: 2 3 4 * +
Resultado: 14
"""

# 🔹 Prioridad de operadores
def prioridad(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


# 🔹 INFija → POSTfija
def infija_a_postfija(expresion):
    pila = []
    salida = []

    for c in expresion:
        if c.isdigit():
            salida.append(c)

        elif c == '(':
            pila.append(c)

        elif c == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()

        else:  # operador
            while pila and prioridad(c) <= prioridad(pila[-1]):
                salida.append(pila.pop())
            pila.append(c)

    while pila:
        salida.append(pila.pop())

    return " ".join(salida)


# 🔹 Evaluar POSTfija
def evaluar_postfija(expresion):
    pila = []

    for token in expresion.split():
        if token.isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()

            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)

    return pila[0]


# 🔥 PROGRAMA PRINCIPAL
expresion = "2+3*4"

postfija = infija_a_postfija(expresion)
resultado = evaluar_postfija(postfija)

print("Expresión infija:", expresion)
print("Expresión postfija:", postfija)
print("Resultado:", resultado)

"""
Convierte una expresión POSTfija a INFija usando una pila.

Ejemplo:
Postfija: "A B C * +"
Infija: (A + (B * C))
"""

def postfija_a_infija(expresion):
    pila = []

    for token in expresion.split():

        # Si es operando (letras o números)
        if token.isalnum():
            pila.append(token)

        else:
            # Sacamos dos operandos
            b = pila.pop()
            a = pila.pop()

            # Formamos la expresión infija con paréntesis
            nueva = f"({a} {token} {b})"
            pila.append(nueva)

    return pila[0]


# 🔥 PRUEBAS
print(postfija_a_infija("A B C * +"))     # (A + (B * C))
print(postfija_a_infija("2 3 +"))         # (2 + 3)
print(postfija_a_infija("2 3 4 * +"))     # (2 + (3 * 4))
print(postfija_a_infija("5 1 2 + 4 * + 3 -"))  # ((5 + ((1 + 2) * 4)) - 3)