import re 

def validar_correo(correo):
    """
    Valida si un correo electrónico es correcto.
    Un correo válido tiene el formato: nombre@dominio.extension
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None


# 🔥 PRUEBAS
print(validar_correo("test@gmail.com"))       # True
print(validar_correo("usuario123@dominio.co")) # True
print(validar_correo("malcorreo.com"))        # False
print(validar_correo("otro@correo"))          # False

import re

def validar_contrasena(password):
    """
    Valida si una contraseña es segura.

    Reglas:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial (@$!%*?&)

    Ejemplo:
    validar_contrasena("Hola123!") -> True
    validar_contrasena("hola123") -> False
    """

    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(patron, password) is not None


# 🔥 PRUEBAS
print(validar_contrasena("Hola123!"))   # True
print(validar_contrasena("hola123"))    # False
print(validar_contrasena("HOLA123!"))   # False
print(validar_contrasena("Hola!"))      # False

import re

def extraer_menciones(texto):
    """
    Extrae todas las menciones de un texto.
    Una mención empieza con @ seguido de letras, números o guion bajo.

    Ejemplo:
    extraer_menciones("Hola @juan y @maria123, revisen esto")
    -> ["@juan", "@maria123"]
    """
    
    patron = r'@\w+'
    return re.findall(patron, texto)


# 🔥 PRUEBA
texto = "Hola @juan y @maria123, revisen esto @dev_python"
resultado = extraer_menciones(texto)

print("Menciones encontradas:")
print(resultado)

"""
Sistema de gestión de tareas.
Cada tarea tiene: nombre, prioridad (1-5) y si está completada.

Se usan listas enlazadas y recursividad.
"""

class Tarea:
    def __init__(self, nombre, prioridad, completada=False):
        self.nombre = nombre
        self.prioridad = prioridad
        self.completada = completada
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.completada else "○"
        return f"[{estado}] {self.nombre} - Prioridad: {self.prioridad}"


class ListaTareas:
    def __init__(self):
        self.cabeza = None

    # 🔹 Agregar tarea al final (recursivo)
    def agregar(self, nombre, prioridad):
        nuevo = Tarea(nombre, prioridad)

        def _agregar(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                _agregar(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            _agregar(self.cabeza)

    # 🔹 Mostrar tareas
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin tareas")
            return

        while actual:
            print(actual)
            actual = actual.siguiente

    # 🔹 Marcar tarea como completada
    def completar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                actual.completada = True
                print("Tarea completada ✅")
                return
            actual = actual.siguiente
        print("Tarea no encontrada ❌")

    # 🔹 Sumar prioridades de tareas pendientes (recursivo)
    def suma_pendientes(self):
        def _sumar(nodo):
            if nodo is None:
                return 0
            if not nodo.completada:
                return nodo.prioridad + _sumar(nodo.siguiente)
            else:
                return _sumar(nodo.siguiente)

        return _sumar(self.cabeza)

    # 🔹 Eliminar tareas completadas (recursivo)
    def eliminar_completadas(self):
        def _eliminar(nodo):
            if nodo is None:
                return None
            if nodo.completada:
                return _eliminar(nodo.siguiente)

            nodo.siguiente = _eliminar(nodo.siguiente)
            return nodo

        self.cabeza = _eliminar(self.cabeza)


# 🔥 PRUEBA
lista = ListaTareas()

lista.agregar("Estudiar", 5)
lista.agregar("Hacer ejercicio", 3)
lista.agregar("Leer", 2)

print("📋 Tareas:")
lista.mostrar()

print("\n✅ Completando tarea:")
lista.completar("Hacer ejercicio")

print("\n📊 Suma de prioridades pendientes:")
print(lista.suma_pendientes())

print("\n🧹 Eliminando completadas:")
lista.eliminar_completadas()

print("\n📋 Tareas finales:")
lista.mostrar()

"""
Sistema de cursos en una universidad.

Cada curso tiene un conjunto de estudiantes inscritos.
Se quiere verificar relaciones entre los cursos usando conjuntos.
"""

# Conjuntos de estudiantes
curso_python = {"Ana", "Carlos", "Diana", "Elena"}
curso_java = {"Carlos", "Diana"}
curso_web = {"Ana", "Elena", "Fernando"}


def es_subconjunto(curso1, curso2):
    """
    Verifica si curso1 es subconjunto de curso2.

    Retorna True si TODOS los estudiantes de curso1
    están en curso2.
    """
    return curso1.issubset(curso2)


def estudiantes_comunes(curso1, curso2):
    """
    Retorna los estudiantes que están en ambos cursos.
    """
    return curso1 & curso2


def estudiantes_unicos(curso1, curso2):
    """
    Retorna los estudiantes que están en curso1 pero NO en curso2.
    """
    return curso1 - curso2


# 🔥 PRUEBAS
print("¿Java es subconjunto de Python?")
print(es_subconjunto(curso_java, curso_python))  # True

print("\n¿Web es subconjunto de Python?")
print(es_subconjunto(curso_web, curso_python))  # False

print("\nEstudiantes en común (Python y Web):")
print(estudiantes_comunes(curso_python, curso_web))

print("\nEstudiantes solo en Python:")
print(estudiantes_unicos(curso_python, curso_web))

"""
Problema de la mochila (Knapsack).

Tienes una mochila con capacidad máxima.
Hay objetos con peso y valor.
Debes elegir cuáles llevar para maximizar el valor sin pasarte del peso.

Usar recursividad + memorización.
"""

def mochila_con_memo(pesos, valores, capacidad, i=0, memo=None):
    """
    pesos: lista de pesos de los objetos
    valores: lista de valores de los objetos
    capacidad: peso máximo permitido
    i: índice actual
    memo: diccionario para guardar resultados

    Retorna el valor máximo posible.
    """
    if memo is None:
        memo = {}

    # Caso base
    if i == len(pesos) or capacidad == 0:
        return 0

    # Clave para memo
    clave = (i, capacidad)

    if clave in memo:
        return memo[clave]

    # Opción 1: NO tomar el objeto
    no_tomar = mochila_con_memo(pesos, valores, capacidad, i + 1, memo)

    # Opción 2: tomar el objeto (si cabe)
    tomar = 0
    if pesos[i] <= capacidad:
        tomar = valores[i] + mochila_con_memo(
            pesos, valores, capacidad - pesos[i], i + 1, memo
        )

    # Guardamos el mejor resultado
    memo[clave] = max(tomar, no_tomar)
    return memo[clave]


# 🔥 PRUEBA
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5

print("Valor máximo en la mochila:")
print(mochila_con_memo(pesos, valores, capacidad))  # 7


"""
Problema de cambio de monedas.

Dado un conjunto de monedas y un valor objetivo,
calcular cuántas formas hay de formar ese valor.
"""

# 🔹 SIN MEMORIZACIÓN
def cambio_monedas_sin_memo(monedas, objetivo, i=0):
    # Casos base
    if objetivo == 0:
        return 1
    if objetivo < 0 or i == len(monedas):
        return 0

    # Usar moneda actual
    usar = cambio_monedas_sin_memo(monedas, objetivo - monedas[i], i)

    # No usar moneda actual
    no_usar = cambio_monedas_sin_memo(monedas, objetivo, i + 1)

    return usar + no_usar


# 🔹 CON MEMORIZACIÓN
def cambio_monedas_con_memo(monedas, objetivo, i=0, memo=None):
    if memo is None:
        memo = {}

    # Casos base
    if objetivo == 0:
        return 1
    if objetivo < 0 or i == len(monedas):
        return 0

    clave = (i, objetivo)

    if clave in memo:
        return memo[clave]

    # Usar moneda actual
    usar = cambio_monedas_con_memo(monedas, objetivo - monedas[i], i, memo)

    # No usar moneda actual
    no_usar = cambio_monedas_con_memo(monedas, objetivo, i + 1, memo)

    memo[clave] = usar + no_usar
    return memo[clave]


# 🔥 PRUEBAS
monedas = [1, 2, 5]
objetivo = 5

print("Sin memo:")
print(cambio_monedas_sin_memo(monedas, objetivo))  # 4

print("\nCon memo:")
print(cambio_monedas_con_memo(monedas, objetivo))  # 4