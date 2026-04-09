#monedas [1,5,10,25] Cuantas monedas necesito para un valor (combinaciones) de forma recursiva
def contar_monedas(monedas, valor):
    if valor == 0:
        return 1
    if valor < 0 or not monedas:
        return 0
    return contar_monedas(monedas, valor - monedas[0]) + contar_monedas(monedas[1:], valor)
#codigo de prueba
if __name__ == "__main__":
    monedas = [1, 5, 10, 25]
    valor = 30
    print(f"Cantidad de combinaciones para {valor} con monedas {monedas}: {contar_monedas(monedas, valor)}")

#con memorizacion 
def contar_monedas_mem(monedas, valor, memo=None):
    if memo is None:
        memo = {}
    if valor == 0:
        return 1
    if valor < 0 or not monedas:
        return 0
    if (len(monedas), valor) in memo:
        return memo[(len(monedas), valor)]
    resultado = contar_monedas_mem(monedas, valor - monedas[0], memo) + contar_monedas_mem(monedas[1:], valor, memo)
    memo[(len(monedas), valor)] = resultado
    return resultado
#codigo de prueba
if __name__ == "__main__":
    monedas = [1, 5, 10, 25]
    valor = 30
    print(f"Cantidad de combinaciones para {valor} con monedas {monedas} (con memorización): {contar_monedas_mem(monedas, valor)}")
