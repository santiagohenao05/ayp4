""""En una tienda online tipo Amazon, se desea analizar el historial de compras de un usuario para mejorar las recomendaciones de productos.

Se cuenta con una lista de compras donde algunos productos pueden estar repetidos, ya que el usuario ha comprado varios artículos más de una vez:"""
compras = ["mouse", "teclado", "mouse", "monitor", "teclado", "audifonos"]
catalogo = ["mouse", "teclado", "monitor", "audifonos", "silla", "camara", "tablet"]
"""Construir una nueva lista que contenga únicamente los productos comprados por el usuario sin elementos repetidos.
Determinar cuántas veces se repite cada producto en la lista de compras.
Generar una lista de productos recomendados, considerando aquellos productos del catálogo que el usuario aún no ha comprado.
(Opcional) Ordenar los productos según la cantidad de veces que fueron comprados, de mayor a menor."""
# Eliminar productos repetidos
compras_unicas = list(set(compras))
print("Productos únicos comprados:", compras_unicas)
# Contar la cantidad de veces que se repite cada producto
conteo_compras = {}
for producto in compras:
    if producto in conteo_compras:
        conteo_compras[producto] += 1
    else:
        conteo_compras[producto] = 1
print("Cantidad de veces que se repite cada producto:", conteo_compras)
# Generar lista de productos recomendados
recomendados = [producto for producto in catalogo if producto not in compras_unicas]
print("Productos recomendados:", recomendados)
# (Opcional) Ordenar productos por cantidad de compras
productos_ordenados = sorted(conteo_compras.items(), key=lambda x: x[
1], reverse=True)
print("Productos ordenados por cantidad de compras:", productos_ordenados)
