# def suma_lista(lista):
#     if len(lista) == 0:
#         return 0
#     return lista[0] + suma_lista(lista[1:])

# print(suma_lista([5,3,1,2]))

# ----------- suma con acumulador -----------

def suma_lista(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista(lista[1:], acumulador + lista[0])
print(suma_lista([5,3,1,2]))
