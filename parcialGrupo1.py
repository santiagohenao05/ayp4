import re

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.

    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123

    Ejemplos:
    validar_placa_vehiculo("ABC123") -> True
    validar_placa_vehiculo("ABC-123") -> True
    validar_placa_vehiculo("AB1234") -> False
    validar_placa_vehiculo("abc123") -> False
    """
    
    patron = r'^[A-Z]{3}-?\d{3}$'
    return re.match(patron, placa) is not None
print(validar_placa_vehiculo("ABC123"))

import re

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.

    Ejemplo:
    extraer_hashtags("Hola #python es #genial y #100dias")
    -> ["#python", "#genial", "#100dias"]
    """
    
    patron = r'#\w+'
    return re.findall(patron, texto)
texto = "Hola #python es #genial y #100dias"
print(extraer_hashtags(texto))


class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    # 🔹 Agregar pedido al FINAL (recursivo)
    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)

        def _agregar_recursivo(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                _agregar_recursivo(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            _agregar_recursivo(self.cabeza)

    # 🔹 Mostrar pedidos
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Sin pedidos")
            return

        while actual:
            print(actual)
            actual = actual.siguiente

    # 🔹 Marcar pedido como entregado
    def marcar_entregado(self, cliente):
        actual = self.cabeza
        while actual:
            if actual.cliente == cliente:
                actual.entregado = True
                print("Pedido entregado ✅")
                return
            actual = actual.siguiente
        print("Pedido no encontrado ❌")

    # 🔹 Suma de pedidos NO entregados (recursivo)
    def valor_pendiente(self):
        def _sumar(nodo):
            if nodo is None:
                return 0
            if not nodo.entregado:
                return nodo.valor + _sumar(nodo.siguiente)
            else:
                return _sumar(nodo.siguiente)

        return _sumar(self.cabeza)

    # 🔹 Eliminar pedidos entregados (recursivo)
    def eliminar_entregados(self):
        def _eliminar(nodo):
            if nodo is None:
                return None
            if nodo.entregado:
                return _eliminar(nodo.siguiente)

            nodo.siguiente = _eliminar(nodo.siguiente)
            return nodo

        self.cabeza = _eliminar(self.cabeza)


# 🔥 PROGRAMA DE PRUEBA
lista = ListaPedidos()

lista.agregar("Juan", "Calle 10", 25000)
lista.agregar("Maria", "Carrera 5", 18000)
lista.agregar("Carlos", "Av 80", 32000)

print("📦 Pedidos:")
lista.mostrar()

print("\n🚚 Marcando como entregado:")
lista.marcar_entregado("Maria")

print("\n📊 Valor pendiente:")
print(lista.valor_pendiente())

print("\n🧹 Eliminando entregados:")
lista.eliminar_entregados()

print("\n📦 Pedidos finales:")
lista.mostrar()


# Conjuntos de clubes
club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    (Intersección de los tres)
    """
    return club_ciencias & club_deportes & club_arte


def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.
    """
    solo_ciencias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_ciencias - club_deportes

    return solo_ciencias | solo_deportes | solo_arte


def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.
    """
    clubes = []

    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")

    return clubes


# 🔥 PRUEBAS
print("En los tres clubes:")
print(estudiantes_en_todos())  # set()

print("\nEn exactamente un club:")
print(solo_un_club())  # {'Elena', 'Hugo', 'Isabel', 'Julia', 'Karen'}

print("\nClubes de Carlos:")
print(clubes_de_estudiante("Carlos"))  # ['Ciencias', 'Deportes']

print("\nClubes de Julia:")
print(clubes_de_estudiante("Julia"))  # ['Arte']

def escalones_sin_memo(n):
    """
    Calcula de cuántas formas se puede subir una escalera de n escalones.
    Usando recursividad pura.
    """
    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Caso recursivo
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)


def escalones_con_memo(n, memo=None):
    """
    Misma función pero usando memorización (diccionario).
    """
    if memo is None:
        memo = {}

    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Si ya está calculado, lo retornamos
    if n in memo:
        return memo[n]

    # Lo calculamos y guardamos
    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]


# 🔥 PRUEBAS
print("Sin memo:")
print(escalones_sin_memo(4))  # 5

print("\nCon memo:")
print(escalones_con_memo(10))  # 89
print(escalones_con_memo(30))  # 1346269