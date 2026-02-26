"""
Google Chrome te ha contratado para implementar el historial de navegación.
Debes diseñar e implementar el sistema usando listas enlazadas.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Pagina) con los atributos necesarios
2. Diseñar la clase Lista (Historial) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------

a) Clase NODO (Pagina):
   - Debe almacenar: URL, título de la página, tiempo en segundos
   - Debe poder enlazarse con otra página

b) Clase LISTA (Historial):
   - Debe mantener referencia al inicio de la lista
   - Las páginas más recientes van al INICIO
"""
class Pagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo
        self.siguiente = None
"""
b) Clase LISTA (Historial):
   - Debe mantener referencia al inicio de la lista
   - Las páginas más recientes van al INICIO
"""
class Historial:
    def __init__(self):
        self.inicio = None

    def agregar_pagina(self, url, titulo, tiempo):
        nueva_pagina = Pagina(url, titulo, tiempo)
        nueva_pagina.siguiente = self.inicio
        self.inicio = nueva_pagina  
    def tiempo_total(self):
        def calcular_tiempo(pagina):
            if pagina is None:
                return 0
            return pagina.tiempo + calcular_tiempo(pagina.siguiente)
        return calcular_tiempo(self.inicio)
    def buscar_por_dominio(self, dominio):
        def buscar(pagina):
            if pagina is None:
                return None
            if dominio in pagina.url:
                nueva_lista.agregar_pagina(pagina.url, pagina.titulo, pagina.tiempo)
            buscar(pagina.siguiente)
        nueva_lista = Historial()
        buscar(self.inicio)
        return nueva_lista
    def eliminar_paginas_rapidas(self, tiempo_limite):
        def eliminar(pagina):
            if pagina is None:
                return None
            if pagina.tiempo < tiempo_limite:
                return eliminar(pagina.siguiente)
            pagina.siguiente = eliminar(pagina.siguiente)
            return pagina
        self.inicio = eliminar(self.inicio)
# Ejemplo de uso
if __name__ == "__main__":
    historial = Historial()
    historial.agregar_pagina("https://www.youtube.com", "YouTube", 120)
    historial.agregar_pagina("https://www.google.com", "Google", 30)
    historial.agregar_pagina("https://www.facebook.com", "Facebook", 45)

    print("Tiempo total de navegación:", historial.tiempo_total())

    dominio_busqueda = "youtube"
    paginas_encontradas = historial.buscar_por_dominio(dominio_busqueda)
    print(f"Páginas que contienen '{dominio_busqueda}':")
    pagina_actual = paginas_encontradas.inicio
    while pagina_actual:
        print(f"- {pagina_actual.url} ({pagina_actual.titulo})")
        pagina_actual = pagina_actual.siguiente

    tiempo_limite = 40
    historial.eliminar_paginas_rapidas(tiempo_limite)
    print(f"Historial después de eliminar páginas con tiempo < {tiempo_limite} segundos:")
    pagina_actual = historial.inicio
    while pagina_actual:
        print(f"- {pagina_actual.url} ({pagina_actual.titulo}) - {pagina_actual.tiempo} segundos")
        pagina_actual = pagina_actual.siguiente

    
             
    