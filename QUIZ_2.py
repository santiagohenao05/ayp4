"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════
"""

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 1: SUDOKU
# ═══════════════════════════════════════════════════════════════════════════════

def validar_fila(tablero, num_fila):
    fila = set(tablero[num_fila])
    return fila == NUMEROS_VALIDOS


def validar_columna(tablero, num_columna):
    columna = set()
    for i in range(9):
        columna.add(tablero[i][num_columna])
    return columna == NUMEROS_VALIDOS


def validar_subcuadro(tablero, fila_inicio, col_inicio):
    subcuadro = set()
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            subcuadro.add(tablero[i][j])
    return subcuadro == NUMEROS_VALIDOS


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 2: CONJUNTOS CON LISTAS LIGADAS
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

def es_subconjunto(conjunto_a, conjunto_b):
    actual = conjunto_a.cabeza
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True


def tiene_permisos(permisos_usuario, permisos_requeridos):
    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)
    
    print("\n📋 Validando filas:")
    for i in range(9):
        resultado = validar_fila(TABLERO, i)
        print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")
    
    print("\n📋 Validando columnas:")
    for j in range(9):
        resultado = validar_columna(TABLERO, j)
        print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")
    
    print("\n📋 Validando subcuadros 3x3:")
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            resultado = validar_subcuadro(TABLERO, fi, ci)
            print(f"  Subcuadro ({fi+1},{ci+1}): {'✓' if resultado else '✗'}")
    
    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)
    
    admin = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])
    editor = Conjunto(["leer", "escribir"])
    viewer = Conjunto(["leer"])
    
    print(f"\n👤 Roles definidos:")
    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")
    
    print(f"\n🔍 Verificando subconjuntos:")
    print(f"  ¿Viewer ⊆ Editor? {es_subconjunto(viewer, editor)}")
    print(f"  ¿Editor ⊆ Admin? {es_subconjunto(editor, admin)}")
    print(f"  ¿Admin ⊆ Editor? {es_subconjunto(admin, editor)}")
    
    print(f"\n🔐 Verificando permisos:")
    
    accion_editar = Conjunto(["leer", "escribir"])
    accion_admin = Conjunto(["crear_usuarios", "eliminar"])
    
    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")
    
    print(f"\n  ¿Editor puede editar? {tiene_permisos(editor, accion_editar)}")
    print(f"  ¿Viewer puede editar? {tiene_permisos(viewer, accion_editar)}")
    print(f"  ¿Admin puede hacer acción admin? {tiene_permisos(admin, accion_admin)}")
    print(f"  ¿Editor puede hacer acción admin? {tiene_permisos(editor, accion_admin)}")