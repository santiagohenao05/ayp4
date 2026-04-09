"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1a: Clase Nodo (Cliente)
# Debe almacenar: nombre, tipo de atención y tiempo
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, nombre, tipo, tiempo):
        self.nombre = nombre
        self.tipo = tipo  # "preferencial" o "normal"
        self.tiempo = tiempo
        self.siguiente = None


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1b: Clase Lista (Cola)
# - Preferenciales al inicio
# - Normales al final
# ═══════════════════════════════════════════════════════════════════════════════

class Cola:
    def __init__(self):
        self.cabeza = None

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 2: AGREGAR CLIENTE (RECURSIVO)
    # - Preferencial: antes de los normales
    # - Normal: al final
    # ═══════════════════════════════════════════════════════════════════════════
    
    def agregar(self, nombre, tipo, tiempo):
        nuevo = Nodo(nombre, tipo, tiempo)
        
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            if tipo == "preferencial":
                self.cabeza = self._agregar_preferencial(self.cabeza, nuevo)
            else:
                self._agregar_normal(self.cabeza, nuevo)

    # Método recursivo para insertar preferenciales
    def _agregar_preferencial(self, actual, nuevo):
        # Si encuentra un normal, inserta antes
        if actual.tipo == "normal":
            nuevo.siguiente = actual
            return nuevo
        
        # Si llegó al final, agrega
        if actual.siguiente is None:
            actual.siguiente = nuevo
            return actual
        
        actual.siguiente = self._agregar_preferencial(actual.siguiente, nuevo)
        return actual

    # Método recursivo para insertar normales al final
    def _agregar_normal(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
            return
        
        self._agregar_normal(actual.siguiente, nuevo)

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 3: TIEMPO DE ESPERA (RECURSIVO)
    # Suma tiempos de clientes anteriores
    # ═══════════════════════════════════════════════════════════════════════════
    
    def tiempo_espera(self, nombre):
        return self._tiempo_espera(self.cabeza, nombre, 0)

    def _tiempo_espera(self, actual, nombre, acumulado):
        if actual is None:
            return -1
        
        if actual.nombre == nombre:
            return acumulado
        
        return self._tiempo_espera(
            actual.siguiente,
            nombre,
            acumulado + actual.tiempo
        )

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 4: ATENDER SIGUIENTE
    # Retira el primer cliente
    # ═══════════════════════════════════════════════════════════════════════════
    
    def atender(self):
        if self.cabeza is None:
            return None
        
        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return atendido

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 5: CONTAR POR TIPO (RECURSIVO)
    # Retorna (preferenciales, normales)
    # ═══════════════════════════════════════════════════════════════════════════
    
    def contar_por_tipo(self):
        return self._contar(self.cabeza)

    def _contar(self, actual):
        if actual is None:
            return (0, 0)
        
        pref, norm = self._contar(actual.siguiente)
        
        if actual.tipo == "preferencial":
            return (pref + 1, norm)
        else:
            return (pref, norm + 1)

    # ═══════════════════════════════════════════════════════════════════════════
    # MÉTODO EXTRA: Mostrar la cola
    # ═══════════════════════════════════════════════════════════════════════════
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.nombre} ({actual.tipo}, {actual.tiempo} min)")
            actual = actual.siguiente


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)
    
    print("Cola:")
    cola.mostrar()
    
    print("\nEspera de Pedro:", cola.tiempo_espera("Pedro"))
    
    print("\nPor tipo:", cola.contar_por_tipo())
    
    atendido = cola.atender()
    print("\nAtendido:", atendido.nombre if atendido else None)




"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                    Sistema de Inventario de Productos
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1a: Clase Nodo (Producto)
# - nombre, categoría, precio, cantidad
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1b: Clase Lista (Inventario)
# - Mantener orden alfabético por nombre
# ═══════════════════════════════════════════════════════════════════════════════

class Inventario:
    def __init__(self):
        self.cabeza = None

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 2: AGREGAR PRODUCTO (RECURSIVO)
    # - Orden alfabético
    # - Si existe, actualizar cantidad
    # ═══════════════════════════════════════════════════════════════════════════
    
    def agregar(self, nombre, categoria, precio, cantidad):
        nuevo = Nodo(nombre, categoria, precio, cantidad)
        
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, actual, nuevo):
        # Si el producto ya existe → actualizar cantidad
        if actual.nombre == nuevo.nombre:
            actual.cantidad += nuevo.cantidad
            return actual
        
        # Insertar antes si va primero alfabéticamente
        if nuevo.nombre < actual.nombre:
            nuevo.siguiente = actual
            return nuevo
        
        # Si es el final
        if actual.siguiente is None:
            actual.siguiente = nuevo
            return actual
        
        actual.siguiente = self._agregar_rec(actual.siguiente, nuevo)
        return actual

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 3: VALOR TOTAL DEL INVENTARIO (RECURSIVO)
    # suma de (precio * cantidad)
    # ═══════════════════════════════════════════════════════════════════════════
    
    def valor_total(self):
        return self._valor_total(self.cabeza)

    def _valor_total(self, actual):
        if actual is None:
            return 0
        
        return (actual.precio * actual.cantidad) + self._valor_total(actual.siguiente)

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 4: PRODUCTOS CON BAJO STOCK (RECURSIVO)
    # - Retorna nueva lista
    # ═══════════════════════════════════════════════════════════════════════════
    
    def productos_bajo_stock(self, limite):
        nueva_lista = Inventario()
        nueva_lista.cabeza = self._bajo_stock_rec(self.cabeza, limite)
        return nueva_lista

    def _bajo_stock_rec(self, actual, limite):
        if actual is None:
            return None
        
        siguiente = self._bajo_stock_rec(actual.siguiente, limite)
        
        if actual.cantidad < limite:
            nuevo = Nodo(actual.nombre, actual.categoria, actual.precio, actual.cantidad)
            nuevo.siguiente = siguiente
            return nuevo
        
        return siguiente

    # ═══════════════════════════════════════════════════════════════════════════
    # PUNTO 5: ELIMINAR PRODUCTO (RECURSIVO)
    # ═══════════════════════════════════════════════════════════════════════════
    
    def eliminar(self, nombre):
        self.cabeza, eliminado = self._eliminar_rec(self.cabeza, nombre)
        return eliminado

    def _eliminar_rec(self, actual, nombre):
        if actual is None:
            return None, False
        
        if actual.nombre == nombre:
            return actual.siguiente, True
        
        actual.siguiente, eliminado = self._eliminar_rec(actual.siguiente, nombre)
        return actual, eliminado

    # ═══════════════════════════════════════════════════════════════════════════
    # MÉTODO EXTRA: Mostrar inventario
    # ═══════════════════════════════════════════════════════════════════════════
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.nombre} | {actual.categoria} | ${actual.precio} | stock: {actual.cantidad}")
            actual = actual.siguiente


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    inv = Inventario()
    
    # Agregar productos (orden: Arroz, Leche, Pan, Sal)
    inv.agregar("Pan", "Panadería", 2500, 50)
    inv.agregar("Leche", "Lácteos", 4500, 30)
    inv.agregar("Arroz", "Granos", 3200, 100)
    inv.agregar("Sal", "Condimentos", 1500, 5)
    
    print("Inventario:")
    inv.mostrar()
    
    print("\nValor total:", inv.valor_total())
    
    print("\nProductos con bajo stock:")
    bajo_stock = inv.productos_bajo_stock(40)
    bajo_stock.mostrar()
    
    print("\nEliminando Sal...")
    inv.eliminar("Sal")
    inv.mostrar()