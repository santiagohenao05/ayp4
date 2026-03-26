"""En una tienda online tipo Amazon, se quiere recomendar productos a los usuarios según sus compras, pero usando listas normales"""
usuarios = {
    "Santiago": ["mouse", "teclado", "monitor"],
    "Camila": ["teclado", "monitor", "audifonos"],
    "Juan": ["mouse", "silla", "monitor"],
    "Laura": ["audifonos", "teclado"]
}
"""Crear una función que calcule la similitud entre dos usuarios usando listas
(tipo Jaccard pero hecho manualmente)

👉 Debes:

Calcular la intersección recorriendo listas con ciclos
Calcular la unión sin repetir elementos (también manual)
Calcular la similitud entre Santiago y los demás usuarios
Encontrar el usuario más similar a Santiago
Recomendar productos a Santiago:
Productos del usuario más similar
Que Santiago no tenga
BONUS 🔥:
Mostrar todas las recomendaciones posibles sin repetir (hecho manual)"""
#crear una función que calcule la similitud entre dos usuarios usando listas (tipo jaccard pero hecho manualmente)
def indice_jaccard(usuario1, usuario2):
    compras1 = usuarios[usuario1]
    compras2 = usuarios[usuario2]
    
    # Calcular intersección
    interseccion = []
    for producto in compras1:
        if producto in compras2 and producto not in interseccion:
            interseccion.append(producto)
    
    # Calcular unión
    union = []
    for producto in compras1:
        if producto not in union:
            union.append(producto)
    for producto in compras2:
        if producto not in union:
            union.append(producto)
    
    # Evitar división por cero
    if len(union) == 0:
        return 0
    
    # Calcular similitud
    return len(interseccion) / len(union)
#calcular la similitud entre santiago y los demás usuarios
similaridades = {}
for usuario in usuarios:
    if usuario != "Santiago":
        similaridades[usuario] = indice_jaccard("Santiago", usuario)
#encontrar el usuario más similar a santiago
usuario_mas_similar = max(similaridades, key=similaridades.get)

print(f"El usuario más similar a Santiago es: {usuario_mas_similar} con una similitud de {similaridades[usuario_mas_similar]:.2f}")
#recomendar productos a santiago: productos del usuario más similar que santiago no tenga
recomendaciones = []
for producto in usuarios[usuario_mas_similar]:
    if producto not in usuarios["Santiago"] and producto not in recomendaciones:
        recomendaciones.append(producto)    
print(f"Recomendaciones para Santiago basadas en {usuario_mas_similar}: {recomendaciones}")
#mostrar todas las recomendaciones posibles sin repetir (hecho manual)
recomendaciones_unicas = []
for usuario in usuarios:
    if usuario != "Santiago":
        for producto in usuarios[usuario]:
            if producto not in usuarios["Santiago"] and producto not in recomendaciones_unicas:
                recomendaciones_unicas.append(producto)
print(f"Todas las posibles recomendaciones para Santiago: {recomendaciones_unicas}")
