"""En una plataforma tipo Netflix, se quiere recomendar películas a los usuarios según sus gustos.
Cada usuario tiene un conjunto de películas que ya vio."""
usuarios = {
    "Santiago": {"Inception", "Matrix", "Interstellar"},
    "Camila": {"Matrix", "Titanic", "Inception"},
    "Juan": {"Interstellar", "Avatar", "Matrix"},
    "Laura": {"Titanic", "Avatar"},
}
"""Encontrar cuál usuario tiene más películas en común con Santiago
(ese será el usuario más parecido)
Recomendarle a Santiago películas que ese usuario similar haya visto pero él no
Mostrar todas las posibles recomendaciones sin repetir (puedes usar unión)
Verificar si hay algún usuario que tenga exactamente los mismos gustos que Santiago
BONUS 🔥:
Recomendar películas a todos los usuarios, comparándolos entre sí
(tipo: cada usuario recibe recomendaciones basadas en el más parecido)"""
#encontrar el usuario que tiene mas peliculas en comun con santiago
santiago_peliculas = usuarios["Santiago"]
usuario_similar = None
max_comunes = 0
for usuario, peliculas in usuarios.items():
    if usuario != "Santiago":
        comunes = santiago_peliculas.intersection(peliculas)
        if len(comunes) > max_comunes:
            max_comunes = len(comunes)
            usuario_similar = usuario
print(f"El usuario más similar a Santiago es: {usuario_similar} con {max_comunes} películas en común.")
#recomendarle a santiago peliculas que ese usuario similar haya visto pero el no
recomendaciones = usuarios[usuario_similar] - santiago_peliculas
print(f"Recomendaciones para Santiago basadas en {usuario_similar}: {recomendaciones}")
#mostrar todas las posibles recomendaciones sin repetir (puedes usar unión) 
recomendaciones_unicas = set()
for usuario, peliculas in usuarios.items():
    if usuario != "Santiago":
        recomendaciones_unicas = recomendaciones_unicas.union(peliculas - santiago_peliculas)
print(f"Todas las posibles recomendaciones para Santiago: {recomendaciones_unicas}")
#verificar si hay algun usuario que tenga exactamente los mismos gustos que santiago
gustos_iguales = []
for usuario, peliculas in usuarios.items():
    if usuario != "Santiago" and peliculas == santiago_peliculas:
        gustos_iguales.append(usuario)
if gustos_iguales:
    print(f"Usuarios con gustos exactamente iguales a Santiago: {gustos_iguales}")
else:
    print("No hay usuarios con gustos exactamente iguales a Santiago.")
#recomendar peliculas a todos los usuarios, comparandolos entre si (tipo: cada usuario recibe recomendaciones basadas en el mas parecido)
recomendaciones_para_usuarios = {}
for usuario, peliculas in usuarios.items():
    usuario_similar = None
    max_comunes = 0
    for otro_usuario, otras_peliculas in usuarios.items():
        if otro_usuario != usuario:
            comunes = peliculas.intersection(otras_peliculas)
            if len(comunes) > max_comunes:
                max_comunes = len(comunes)
                usuario_similar = otro_usuario
    if usuario_similar:
        recomendaciones_para_usuarios[usuario] = usuarios[usuario_similar] - peliculas
print("Recomendaciones para cada usuario basadas en el usuario más similar:")
for usuario, recomendaciones in recomendaciones_para_usuarios.items():
    print(f"{usuario}: {recomendaciones}")
