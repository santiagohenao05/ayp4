"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 1: IMPLEMENTACIÓN DE PILA (STACK)
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

La Pila es una estructura de datos LIFO (Last In, First Out).
El último elemento en entrar es el primero en salir.

Analogía: Una pila de platos - solo puedes poner o quitar del tope.
"""


class Nodo:
    """Nodo para la lista enlazada"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """
    Implementación de Pila usando lista enlazada.
    Todas las operaciones son O(1).
    """
    
    def __init__(self):
        self.tope = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """Retorna True si la pila está vacía"""
        return self.tope is None
    
    def push(self, dato):
        """Agrega un elemento al tope de la pila - O(1)"""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1
    
    def pop(self):
        """Quita y retorna el elemento del tope - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato
    
    def peek(self):
        """Retorna el elemento del tope sin quitarlo - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        return self.tope.dato
    
    def __len__(self):
        """Retorna el tamaño de la pila"""
        return self.tamanio
    
    def __str__(self):
        """Representación visual de la pila"""
        if self.esta_vacia():
            return "Pila vacía"
        
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return "Tope → " + " → ".join(elementos) + " → None"


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("       DEMOSTRACIÓN DE PILA (STACK)")
    print("=" * 50)
    
    pila = Pila()
    
    print("\n📥 Agregando elementos (push):")
    for valor in [10, 20, 30, 40]:
        pila.push(valor)
        print(f"   push({valor}) → {pila}")
    
    print(f"\n📊 Tamaño de la pila: {len(pila)}")
    print(f"👀 Elemento en el tope (peek): {pila.peek()}")
    
    print("\n📤 Quitando elementos (pop):")
    while not pila.esta_vacia():
        valor = pila.pop()
        print(f"   pop() = {valor} → {pila}")
    
    print("\n" + "=" * 50)
    print("💡 Observa: Los elementos salen en orden inverso")
    print("   al que entraron (LIFO)")
    print("=" * 50)


"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 2: EVALUACIÓN DE EXPRESIONES POSTFIJAS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

Notación Postfija (Polaca Inversa):
- El operador va DESPUÉS de los operandos
- No necesita paréntesis ni reglas de precedencia
- Se evalúa de izquierda a derecha usando una pila

Ejemplos:
    Infija: 3 + 4        →  Postfija: 3 4 +
    Infija: 3 + 4 * 2    →  Postfija: 3 4 2 * +
    Infija: (3 + 4) * 2  →  Postfija: 3 4 + 2 *
"""

from ejemplo_01_pila import Pila


def evaluar_postfija(expresion):
    """
    Evalúa una expresión en notación postfija.
    
    Algoritmo:
    1. Recorrer tokens de izquierda a derecha
    2. Si es número → push a la pila
    3. Si es operador → pop dos operandos, operar, push resultado
    4. Al final, el resultado está en el tope
    
    Args:
        expresion: String con tokens separados por espacios
    
    Returns:
        Resultado numérico de la expresión
    """
    pila = Pila()
    tokens = expresion.split()
    
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b,
        '**': lambda a, b: a ** b,
    }
    
    print(f"\n📝 Evaluando: {expresion}")
    print("-" * 40)
    
    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            # Es un número (soporta negativos y decimales)
            valor = float(token) if '.' in token else int(token)
            pila.push(valor)
            print(f"   Token '{token}' → push({valor})")
        elif token in operadores:
            # Es un operador
            b = pila.pop()  # Segundo operando (sale primero)
            a = pila.pop()  # Primer operando
            resultado = operadores[token](a, b)
            pila.push(resultado)
            print(f"   Token '{token}' → {a} {token} {b} = {resultado}")
        else:
            raise ValueError(f"Token no reconocido: {token}")
        
        print(f"            Pila: {pila}")
    
    return pila.pop()


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("   EVALUACIÓN DE EXPRESIONES POSTFIJAS")
    print("=" * 50)
    
    # Ejemplos de expresiones
    expresiones = [
        ("3 4 +", "3 + 4"),
        ("3 4 2 * +", "3 + 4 * 2"),
        ("3 4 + 2 *", "(3 + 4) * 2"),
        ("5 1 2 + 4 * + 3 -", "5 + (1 + 2) * 4 - 3"),
        ("2 3 ** 4 +", "2 ** 3 + 4"),
        ("10 3 /", "10 / 3"),
    ]
    
    for postfija, infija in expresiones:
        resultado = evaluar_postfija(postfija)
        print(f"\n✅ Resultado: {resultado}")
        print(f"   (Equivale a: {infija} = {eval(infija)})")
        print("=" * 50)

"""
═══════════════════════════════════════════════════════════════════════════════
SOLUCIÓN EJERCICIO 2: VERIFICADOR DE PARÉNTESIS BALANCEADOS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
    
    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


def parentesis_balanceados(expresion):
    """
    Verifica si los paréntesis, corchetes y llaves están balanceados.
    """
    pila = Pila()
    
    # Mapeo de cierre a apertura
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    aperturas = set(pares.values())  # {'(', '[', '{'}
    cierres = set(pares.keys())      # {')', ']', '}'}
    
    for caracter in expresion:
        if caracter in aperturas:
            # Es un símbolo de apertura → push
            pila.push(caracter)
        elif caracter in cierres:
            # Es un símbolo de cierre → verificar
            if pila.esta_vacia():
                return False  # Cierre sin apertura
            
            tope = pila.pop()
            if tope != pares[caracter]:
                return False  # No coinciden
    
    # La pila debe estar vacía al final
    return pila.esta_vacia()


def verificar_con_detalle(expresion):
    """
    Versión extendida que retorna información detallada del error.
    """
    pila = Pila()  # Guardará tuplas (símbolo, posición)
    
    pares = {')': '(', ']': '[', '}': '{'}
    nombres = {'(': 'paréntesis', '[': 'corchete', '{': 'llave',
               ')': 'paréntesis', ']': 'corchete', '}': 'llave'}
    
    aperturas = set(pares.values())
    cierres = set(pares.keys())
    
    for i, caracter in enumerate(expresion):
        if caracter in aperturas:
            pila.push((caracter, i))
        elif caracter in cierres:
            if pila.esta_vacia():
                return (False, f"Error en posición {i}: '{caracter}' sin {nombres[caracter]} de apertura")
            
            tope, pos_apertura = pila.pop()
            esperado = pares[caracter]
            
            if tope != esperado:
                return (False, f"Error en posición {i}: se esperaba cierre para '{tope}' pero se encontró '{caracter}'")
    
    if not pila.esta_vacia():
        simbolo, pos = pila.pop()
        return (False, f"Error: falta cerrar '{simbolo}' abierto en posición {pos}")
    
    return (True, "Expresión válida")


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("   VERIFICADOR DE PARÉNTESIS (SOLUCIÓN)")
    print("=" * 60)
    
    casos_prueba = [
        ("(a + b)", True),
        ("[(a + b) * c]", True),
        ("{[()]}", True),
        ("((()))", True),
        ("", True),
        ("sin paréntesis", True),
        ("(a + b]", False),
        ("((a + b)", False),
        ("a + b)", False),
        ("{[(])}", False),
        ("([)]", False),
    ]
    
    print("\n📊 Resultados función básica:")
    print("-" * 60)
    
    todos_correctos = True
    for expresion, esperado in casos_prueba:
        resultado = parentesis_balanceados(expresion)
        correcto = resultado == esperado
        todos_correctos = todos_correctos and correcto
        estado = "✅" if correcto else "❌"
        expr_mostrar = expresion if expresion else "(vacío)"
        print(f"{estado} '{expr_mostrar}' → {resultado}")
    
    print(f"\n{'✅ Todas las pruebas pasaron' if todos_correctos else '❌ Algunas pruebas fallaron'}")
    
    print("\n" + "=" * 60)
    print("   PRUEBAS CON DETALLE DE ERROR")
    print("=" * 60)
    
    casos_error = [
        "(a + b)",
        "(a + b]",
        "((a + b)",
        "a + b)",
        "{[(])}",
    ]
    
    for expr in casos_error:
        valido, mensaje = verificar_con_detalle(expr)
        estado = "✅" if valido else "❌"
        print(f"\n{estado} '{expr}'")
        print(f"   {mensaje}")

