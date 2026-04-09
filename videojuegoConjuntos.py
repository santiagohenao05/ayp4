"""En una plataforma tipo Steam, los usuarios tienen listas de juegos jugados."""
usuarios = {
    "Santiago": {"FIFA", "Call of Duty", "Minecraft"},
    "Camila": {"Minecraft", "The Sims", "FIFA"},
    "Juan": {"Call of Duty", "Fortnite", "Minecraft"},
    "Laura": {"The Sims", "Stardew Valley"}
}
"""Calcular la similitud de Jaccard entre todos los usuarios
Encontrar el usuario más similar a Santiago
Recomendar juegos a Santiago
Mostrar recomendaciones ordenadas por similitud (mayor a menor)"""
#calcular la similitud de Jaccard entre todos los usuarios  
def indice_jaccard(usuario1, usuario2):
    juegos1 = usuarios[usuario1]
    juegos2 = usuarios[usuario2]
    
    interseccion = juegos1.intersection(juegos2)
    union = juegos1.union(juegos2)
    
    if len(union) == 0:
        return 0
    
    return len(interseccion) / len(union)
similaridades = {}
for usuario in usuarios:
    if usuario != "Santiago":
        similaridades[usuario] = indice_jaccard("Santiago", usuario)
#encontrar el usuario más similar a santiago
usuario_mas_similar = max(similaridades, key=similaridades.get) 
print(f"El usuario más similar a Santiago es: {usuario_mas_similar} con una similitud de {similaridades[usuario_mas_similar]:.2f}")
#recomendar juegos a santiago
recomendaciones = []
for producto in usuarios[usuario_mas_similar]:
    if producto not in usuarios["Santiago"] and producto not in recomendaciones:
        recomendaciones.append(producto)
#mostrar recomendaciones ordenadas por similitud (mayor a menor)
recomendaciones_ordenadas = sorted(recomendaciones, key=lambda x: similaridades[usuario_mas_similar], reverse=True)
print("Recomendaciones para Santiago:")
for juego in recomendaciones_ordenadas:
    print(f"- {juego} (similaridad: {similaridades[usuario_mas_similar]:.2f})") 
    