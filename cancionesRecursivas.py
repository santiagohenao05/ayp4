class nodo:
    def __init__(self, nombre, duracion):
        self.nombre=nombre
        self.duracion=duracion
        self.siguiente=None
        self.anterior=None
    
class Lista:
    def __init__(self):
        self.cabeza=None
        self.cola=None

def vacia(self):
    return self.cabeza is None

def agregar(self, nombre, duracion):
        nuevo=nodo(nombre, duracion)
       
        if self.vacia():
            self.cabeza=nuevo
            self.cola=nuevo
        else: 
            nuevo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo
            self.cabeza=nuevo
        print("cancon agragada",str(nuevo.nombre + str(nuevo.duracion)))

def pasar_adelante(self):
        if self.vacia():
            print("Lista vacia")
            return
        if actual is None:
             actual= self.cabeza
             print("Inciio Fin", end=" ")
             #caso base 
        if actual is None:
             return 
        print("Reproduciendo")
        print (str(actual.nombre)+ "(" + str(actual.duracion)+ ")", end="<->")

        #llamada recursiva
        self.pasar_adelante(actual.siguiente)

def pasar_atras(self):
        if self.vacia():
            print("Lista vacia")
            return
        if actual is None:
             actual= self.cola
             print("Inciio Fin", end=" ")
             #caso base 
        if actual is None:
             return 
        print("Reproduciendo")
        print (str(actual.nombre)+ "(" + str(actual.duracion)+ ")", end="<->")

        #llamada recursiva
        self.pasar_atras(actual.anterior)

def Buscar(self,nombre, actual=None):
        if self.vacia():
             return False
        if actual is None:
             actual=self.cabeza
        
        #caso base 
        if actual is None:
             return False
        #llamada recursiva
        return self.Buscar(nombre,actual.siguiente)

        

