class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
class Conjunto:
    def __init__(self,elementos=None):
        self.cabeza=None
        self.tamanio=0
        if elementos:
            for a in elementos:
                self.agregar(a)
        
    def esta_vacia(self):
        return self.tamanio
    def pertenece(self,x):
        actual=self.cabeza
        while actual:
            if actual.dato==x:
                return True
            actual=actual.siguiente
        return False
    def agregar(self,x):
        if self.pertenece(x):
            return False
        nuevo=Nodo(x)
        nuevo.siguiente=self.cabeza
        self.cabeza=nuevo
        self.tamanio+=1
        return True
    def eliminar(self,x):
        if self.esta_vacia():
            return False    
        if self.cabeza.dato==x:
            self.cabeza=self.cabeza.siguiente
            self.tamanio-=1
            return True
        actual=self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato==x:
                actual.siguiente=actual.siguiente.siguiente
                self.tamanio-=1
                return True
            actual=actual.siguiente
        return False
    def vaciar(self):
        self.cabeza=None
        self.tamanio=0  

    def union(self,otro_conjunto): #elementos que estan en A o en B
        resultado=Conjunto()
        actual=self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual=actual.siguiente
        actual=otro_conjunto.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual=actual.siguiente
        return resultado
    def interseccion(self,otro_conjunto): #elementos que estan en A y en B
        resultado=Conjunto()
        actual=self.cabeza
        while actual:
            if otro_conjunto.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual=actual.siguiente
        return resultado
    def diferencia(self,otro_conjunto): #elementos de A que no estan en B
        resultado=Conjunto()
        actual=self.cabeza
        while actual:
            if not otro_conjunto.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual=actual.siguiente
        return resultado
    def diferencia_simetrica(self,otro_conjunto): #elementos que estan en A o en B pero no en ambos
        return self.diferencia(otro_conjunto).union(otro_conjunto.diferencia(self))
    
    def a_lista(self): #devuelve una lista con los elementos del conjunto
        resultado=[]
        actual=self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual=actual.siguiente
        return resultado
    
    def __str__(self): #devuelve una cadena con los elementos del conjunto
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"

A=Conjunto(["A", "B", "C", "D"])
B=Conjunto(["C", "D", "E", "F"])
C=A.union(B)
print(C)