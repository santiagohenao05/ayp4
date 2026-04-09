#crear pila con nodos
import token


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
def esta_vacia (self):
    return self.tope is None

def push(self,dato):
    self.tope=nuevo
    self.tamaño=1
def pop(self):
    if self.esta_vacia():
        return None
    dato=self.tope.dato
    self.tope=self.tope.siguiente
    self.tamaño-=1
    return dato
def peek(self):
    if self.esta_vacia():
        return None
    return self.tope.dato

#diccionario con los operadores lambda
operadores={
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y
}
def evaluar_expresion(expresion):
    pila=Nodo()
    for token in expresion.split():
        if token in operadores:
            b=pila.pop()
            a=pila.pop()
            resultado=operadores[token](a,b)
            pila.push(resultado)
        else:
            pila.push(float(token))
    return pila.pop()

#c_{onvertir innfija a postfija
def infija_a_postfija(expresion):
    precedencia={
        '+':1,
        '-':1,
        '*':2,
        '/':2
    }
    salida=[]
    pila=Pila()
    expresion=expresion.replace(' ','')
    

    elif token in precedencia:
        # Es un operador
        while (not pila.esta_vacia() and
            pila.peek() != '(' and
            pila.peek() in precedencia and
            precedencia[pila.peek()] >= precedencia[token]):
            
        salida.append(pila.pop())

        pila.push(token)
        print(f"    '{token}' (operador) -> pila")

    print(f"    Salida: {salida}")
    print(f"    Pila: {pila}")


