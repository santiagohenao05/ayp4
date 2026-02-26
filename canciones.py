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
        print ("Inicio Fin", end=" ")
        actual=self.cabeza
        elementos=[]
        while actual:
            print("reproduciendo")
            elementos.append(str(actual.nombre) + "(" + str(actual.duracion)+")")
            actual=actual.siguiente
        print("<->".join(elementos))

    def pasar_atras(self):
        if self.vacia():
            print("Lista vacia")
            return
        print ("Inicio Fin", end=" ")
        actual=self.cola
        elementos=[]
        while actual:
            print("reproduciendo")
            elementos.append(str(actual.nombre) + "(" + str(actual.duracion)+")")
            actual=actual.anterior
        print("<->".join(elementos))

    def Buscar(self,nombre):
        actual=self.cabeza
        while actual:
            if actual.nombre==nombre:
                return True
            actual=actual.siguiente
        return False
    
    
if __name__=="__main__":

    lista=Lista()
    lista = Lista()
opcion = ""

while opcion != "6":
    print(" MENÚ ")
    print("1: Agregar canciones")
    print("2: Pasar adelante")
    print("3: Pasar atrás")
    print("4: Buscar canción por nombre")
    print("6: Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            print("Agregando canciones...")
            lista.agregar("Rpiñata", 90)
            lista.agregar("Mano al piso", 100)
            lista.agregar("Fanático", 120)

        case "2":
            print("Pasando canción hacia adelante")
            lista.pasar_adelante()

        case "3":
            print("Pasando canción hacia atrás")
            lista.pasar_atras()

        case "4":
            print("Buscando canción")
            print(f"¿Existe repiñata {lista.Buscar("Rpiñata")}")
            print(f"¿Existe mano al piso? {lista.Buscar("Mano al piso")}")

        case "6":
            print("Saliendo")

        case _:
            print("Opción no válida")

       

        
     
    
    
    print (lista)
