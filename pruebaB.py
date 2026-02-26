#hacer la clase nodo(tarea)
class Nodo: 
    def __init__(self, descripcion, prioridad, estado):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.siguiente = None   
#hacer la clase lista(listaTareas)
class ListaTareas:  
    def __init__(self):
        self.inicio = None
    def agregar_tarea(self, descripcion, prioridad, estado):
        nueva_tarea = Nodo(descripcion, prioridad, estado)
        if self.inicio is None or self.inicio.prioridad < prioridad:
            nueva_tarea.siguiente = self.inicio
            self.inicio = nueva_tarea
        else:
            def insertar(tarea_actual):
                if tarea_actual.siguiente is None or tarea_actual.siguiente.prioridad < prioridad:
                    nueva_tarea.siguiente = tarea_actual.siguiente
                    tarea_actual.siguiente = nueva_tarea
                else:
                    insertar(tarea_actual.siguiente)
            insertar(self.inicio)
#agregar nueva tarea
    def contar_pendientes(self, prioridad):
        def contar(tarea_actual):
            if tarea_actual is None:
                return 0
            if tarea_actual.prioridad == prioridad and not tarea_actual.estado:
                return 1 + contar(tarea_actual.siguiente)
            return contar(tarea_actual.siguiente)
        return contar(self.inicio)
#obtener urgentes
    def obtener_urgentes(self): 
        def obtener(tarea_actual):
            if tarea_actual is None:
                return None
            if tarea_actual.prioridad >= 4 and not tarea_actual.estado:
                nueva_lista.agregar_tarea(tarea_actual.descripcion, tarea_actual.prioridad, tarea_actual.estado)
            obtener(tarea_actual.siguiente)
        nueva_lista = ListaTareas()
        obtener(self.inicio)
        return nueva_lista
#limpiar completadas
    def limpiar_completadas(self):
        def limpiar(tarea_actual):
            if tarea_actual is None:
                return None
            if tarea_actual.estado:
                return limpiar(tarea_actual.siguiente)
            tarea_actual.siguiente = limpiar(tarea_actual.siguiente)
            return tarea_actual
        self.inicio = limpiar(self.inicio)
#codigo de prueba
if __name__ == "__main__":
    lista = ListaTareas()
    lista.agregar_tarea("Tarea 1", 5, False)
    lista.agregar_tarea("Tarea 2", 3, True)
    lista.agregar_tarea("Tarea 3", 4, False)
    print("Pendientes de prioridad 5:", lista.contar_pendientes(5))
    urgentes = lista.obtener_urgentes()
    print("Tareas urgentes pendientes:")
    tarea_actual = urgentes.inicio
    while tarea_actual:
        print(f"- {tarea_actual.descripcion} (Prioridad: {tarea_actual.prioridad})")
        tarea_actual = tarea_actual.siguiente
    lista.limpiar_completadas()
    print("Lista después de limpiar completadas:")
    tarea_actual = lista.inicio
    while tarea_actual:
        estado = "Completada" if tarea_actual.estado else "Pendiente"
        print(f"- {tarea_actual.descripcion} (Prioridad: {tarea_actual.prioridad}, Estado: {estado})")
        tarea_actual = tarea_actual.siguiente
