class Nodo:
    def __init__(self, valor):
        self.valor= valor
        self.siguiente= None

    def es_vacio(self):
        return self.valor is None
class Pila:
    def __init__(self):
        self.tope= None
        self.tamaño= 0
    
    def push(self, valor):
        nuevo_nodo= Nodo(valor)
        nuevo_nodo.siguiente= self.tope
        self.tope= nuevo_nodo
        self.tamaño += 1
    
    def pop(self):
        if self.tamaño == 0:
            raise IndexError("La pila está vacía")
        valor= self.tope.valor
        self.tope= self.tope.siguiente
        self.tamaño -= 1
        return valor 
    
    def peek(self):
        if self.tamaño == 0:
            raise IndexError("La pila está vacía")
        return self.tope.valor
    
    def esta_vacia(self):
        return self.tamaño == 0
def es_correcta(expresion):
    pila= Pila()
    pares= {'(': ')', '{': '}', '[': ']'}
    for token in expresion:
        if token in pares:
            pila.push(token)
        elif token in pares.values():
            if pila.esta_vacia() or pares[pila.pop()] != token:
                return False
    return pila.esta_vacia()
# Ejemplo de uso
expresion1= "{[(}]]"
expresion2= "{[(])}"
print(es_correcta(expresion1))  # Debería imprimir: True
print(es_correcta(expresion2))  # Debería imprimir: False
