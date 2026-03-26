"""En una tienda online tipo Mercado Libre, los productos están organizados por categorías, no por usuarios."""
categorias = {
    "Tecnologia": {"laptop", "mouse", "teclado", "monitor"},
    "Hogar": {"sarten", "licuadora", "microondas"},
    "Deporte": {"balon", "pesas", "bicicleta"},
    "Audio": {"audifonos", "parlante", "microfono"}
}
usuario = {"mouse", "teclado", "audifonos"}

"""Encontrar a qué categorías pertenece el usuario

👉 Revisar en qué categorías aparecen los productos que compró

2. Construir el perfil del usuario

👉 Un conjunto con las categorías que le interesan

3. Calcular similitud de Jaccard entre el usuario y cada categoría

💡 Comparas:

Usuario (productos que tiene)
Categoría (productos que contiene)
Encontrar la categoría más similar
5. Recomendar productos

👉 Productos de esa categoría que el usuario no haya comprado

🔥 BONUS:
Recomendar productos de todas las categorías con similitud > 0.2
Ordenar las categorías por similitud
Mostrar resultados así:"""
#encontrar a qué categorías pertenece el usuario
categorias_usuario = set()  
for categoria, productos in categorias.items():
    if usuario.intersection(productos):
        categorias_usuario.add(categoria)
#calcular similitud de jaccard entre el usuario y cada categoría
similaridades = {}
for categoria, productos in categorias.items():
    interseccion = usuario.intersection(productos)
    union = usuario.union(productos)
    
    if len(union) > 0:
        similaridades[categoria] = len(interseccion) / len(union)
#encontrar la categoría más similar
categoria_mas_similar = max(similaridades, key=similaridades.get)
print(f"La categoría más similar al usuario es: {categoria_mas_similar} con una similitud de {similaridades[categoria_mas_similar]:.2f}")
#recomendar productos de esa categoría que el usuario no haya comprado
recomendaciones = []
for producto in categorias[categoria_mas_similar]:
    if producto not in usuario and producto not in recomendaciones:
        recomendaciones.append(producto)
print(f"Recomendaciones para el usuario basadas en la categoría {categoria_mas_similar}:")
for producto in recomendaciones:
    print(f"- {producto} (similaridad: {similaridades[categoria_mas_similar]:.2f})")
#recomendar productos de todas las categorías con similitud > 0.2
recomendaciones_todas = []  
for categoria, similitud in similaridades.items():
    if similitud > 0.2:
        for producto in categorias[categoria]:
            if producto not in usuario and producto not in recomendaciones_todas:
                recomendaciones_todas.append((producto, similitud))
#ordenar las categorías por similitud
recomendaciones_todas.sort(key=lambda x: x[1], reverse=True)
#mostrar resultados
print("Recomendaciones para el usuario basadas en todas las categorías con similitud > 0.2:")
for producto, similitud in recomendaciones_todas:
    print(f"- {producto} (similaridad: {similitud:.2f})")

