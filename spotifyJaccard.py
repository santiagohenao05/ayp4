"""En una plataforma tipo Spotify, se quiere recomendar canciones a los usuarios comparando sus gustos musicales.
Cada usuario tiene un conjunto de canciones que ha escuchado."""
usuarios = {
    "Santiago": {"Feid - Normal", "Bad Bunny - Yonaguni", "Karol G - Provenza"},
    "Camila": {"Feid - Normal", "Karol G - Provenza", "Shakira - TQG"},
    "Juan": {"Bad Bunny - Yonaguni", "Anuel - China", "Feid - Normal"},
    "Laura": {"Shakira - TQG", "Karol G - Provenza"}
}
"""Crear una función que calcule la similitud de Jaccard entre dos usuarios
Calcular la similitud entre Santiago y todos los demás usuarios
Determinar cuál es el usuario más similar a Santiago (mayor Jaccard)
Recomendarle a Santiago canciones que:
El usuario más similar haya escuchado
Pero Santiago no tenga
BONUS 🔥:
Mostrar una tabla (o prints) con la similitud de todos contra todos"""

#crear una función que calcule la similitud de Jaccard entre dos usuarios
def indice_jaccard(usuario1, usuario2):
    canciones1 = usuarios[usuario1]
    canciones2 = usuarios[usuario2]
    interseccion = canciones1.intersection(canciones2)
    union = canciones1.union(canciones2)
    if len(union) == 0:
        return 0
    return len(interseccion) / len(union)
#calcular la similitud entre santiago y todos los demás usuarios
similaridades = {}  
for usuario in usuarios:
    if usuario != "Santiago":
        similaridades[usuario] = indice_jaccard("Santiago", usuario)
#determinar cuál es el usuario más similar a santiago (mayor jaccard)
usuario_mas_similar = max(similaridades, key=similaridades.get)
print(f"El usuario más similar a Santiago es: {usuario_mas_similar} con una similitud de {similaridades[usuario_mas_similar]:.2f}")
#recomendarle a santiago canciones que el usuario más similar haya escuchado pero santiago no tenga
recomendaciones = usuarios[usuario_mas_similar] - usuarios["Santiago"]  
print(f"Recomendaciones para Santiago basadas en {usuario_mas_similar}: {recomendaciones}")
#mostrar una tabla (o prints) con la similitud de todos contra todos
print("\nSimilitud de Jaccard entre usuarios:")
for usuario1 in usuarios:
    for usuario2 in usuarios:
        if usuario1 != usuario2:
            similitud = indice_jaccard(usuario1, usuario2)
            print(f"{usuario1} vs {usuario2}: {similitud:.2f}")
