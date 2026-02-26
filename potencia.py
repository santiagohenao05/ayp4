# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     return base * potencia(base, exponente - 1)

# print(potencia(2, 3)) # 8

# -------------- Potencia con acumulador --------------
def potencia_tail(base, exponente, acumulador=1):
    if exponente == 0:
        return acumulador
    return potencia_tail(base, exponente - 1, acumulador * base)

print(potencia_tail(2, 3)) # 8