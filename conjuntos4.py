"""redes={
    "Pablo", "camila", "Diego", "Karla", "Esteban"
}
base_datos={
    "Carlos","Diana","Elena","Fernando","Gabriela","Hector","Isabel","Jorge","Karla","Luis"
}
algoritmos={
    "Ana", "Pablo", "Sofia", "Diego", "Laura", "Juan", "Maria", "Pedro", "Luis", "Karla"
}
#cuales estudiantes estan solo en una materia
solo_redes = redes - base_datos - algoritmos
solo_base = base_datos - redes - algoritmos
solo_algoritmos = algoritmos - redes - base_datos

resultado = solo_redes | solo_base | solo_algoritmos

print(resultado)

#cuantos estudiantes hay 
todos = redes | base_datos | algoritmos
print(len(todos)) 

if algoritmos<=base_datos: #algoritmos es subconjunto de base de datos
    print("algoritmos es subconjunto de base de datos")"""

#diccionario de un catalogo de peliculas
Catalogo_peliculas = {
    "Inception": {"Acción", "Ciencia ficción", "Thriller"},
    "The Matrix": {"Acción", "Ciencia ficción"},
    "titanic": {"Drama", "Romance","historica"},
    "The notebook": {"Drama", "Romance"},
    "Avengers": {"Acción", "Ciencia ficción", "Aventura"},
    "John wick": {"Acción", "Crimen", "Thriller"},
    "Interstellar": {"Acción", "Ciencia ficción", "Drama"},
    "The Godfather": {"Crimen", "Drama"},
    "Toy story": {"Animación", "Aventura", "Comedia"},
    "Shrek": {"Animación", "Aventura", "Comedia"}
}

#Encontrar peliculas similares, que compartan minimo dos generos
pelicula = "Inception"
generos_pelicula = Catalogo_peliculas[pelicula]
peliculas_similares = set()
for pelicula, generos in Catalogo_peliculas.items():
    if pelicula != "Inception":
        generos_comunes = generos_pelicula.intersection(generos)
        if len(generos_comunes) >= 2:
            peliculas_similares.add(pelicula)
print(peliculas_similares)

favoritos = {"Acción", "Crimen", "Aventura"}
#recomendar peliculas segun mis generos favoritos y con que porcentaje
recomendaciones = {}
for pelicula, generos in Catalogo_peliculas.items():
    generos_comunes = favoritos.intersection(generos)
    if generos_comunes:
        porcentaje = len(generos_comunes) / len(favoritos) * 100
        recomendaciones[pelicula] = porcentaje
print(recomendaciones)
#mostrar todos los generos que hay en el catalogo
genero_unicos=set() #guarda elementos sin repetir
for generos in Catalogo_peliculas.values():
    generos_unicos=genero_unicos.union(generos)
generos_ordenados=sorted(genero_unicos)
print(generos_ordenados)

#peliculas por genero con operacioens entre conjuntos 
peliculas_por_genero = {}  # Diccionario donde cada género será clave y tendrá una lista de películas
for pelicula, generos in Catalogo_peliculas.items():  # Recorremos cada película y sus géneros
    for genero in generos:  # Recorremos cada género de la película
        if genero not in peliculas_por_genero: peliculas_por_genero[genero] = []  # Si no existe el género, lo creamos con lista vacía
        peliculas_por_genero[genero].append(pelicula)  # Agregamos la película al género correspondiente
print(peliculas_por_genero)  # Mostramos el resultado final

"""Lógica fácil

Crear un diccionario vacío porque se necesita guardar infromacionq mientras recorre datos
NO ES CONJUNTO PORQUE EL SET SOLO GUARDA VALORES PERO SE NECESITAN RELACIOANR COSAS
Recorrer cada película

Recorrer sus géneros

Por cada género, guardar la película ahí

Si el género no existe → lo creo CON UNA CLAVE Y UNA LISTA VACIA PARA GUARDAR PELICULAS

Si ya existe → agrego la película"""
#metodo qeu reciba dos peliculas y devuelva el indice de similitud jaccard
def indice_jaccard(pelicula1, pelicula2):
    generos1 = Catalogo_peliculas[pelicula1]
    generos2 = Catalogo_peliculas[pelicula2]
    interseccion = generos1.intersection(generos2)
    union = generos1.union(generos2)
    if len(union) == 0:
        return 0
    return len(interseccion) / len(union)
similaridad = indice_jaccard("Inception", "The Matrix")
print(similaridad)

STOPWORDS={"el","la","los","las","un","una","unos","unas","de","del","al","y","o","que","en","a",}
#leer dos textos y calcular su indice de similitdu ignorando las stopwords, si el indica es mayor a 0.6, se copiaron
# Conjunto de palabras que no aportan mucho significado (artículos, conectores, etc.)
STOPWORDS = {"el","la","los","las","un","una","unos","unas","de","del","al","y","o","que","en","a"}

# Función que calcula el índice de Jaccard entre dos textos
def indice_jaccard_textos(texto1, texto2):
    
    # Convertimos a minúsculas, separamos en palabras, las pasamos a conjunto
    # y eliminamos las stopwords
    palabras1 = set(texto1.lower().split()) - STOPWORDS
    palabras2 = set(texto2.lower().split()) - STOPWORDS
    
    # Calculamos las palabras en común
    interseccion = palabras1.intersection(palabras2)
    
    # Calculamos todas las palabras sin repetir
    union = palabras1.union(palabras2)
    
    # Evitamos división por cero si no hay palabras
    if len(union) == 0:
        return 0
    
    # Retornamos la similitud (Jaccard)
    return len(interseccion) / len(union)


# Textos de prueba
texto1 = "El gato se subió al árbol y se quedó allí"
texto2 = "El perro se subió al árbol y se quedó allí"

# Calculamos la similitud entre los textos
similaridad_textos = indice_jaccard_textos(texto1, texto2)

# Mostramos el resultado
print(similaridad_textos)

"""Quito palabras que no importan (stopwords)

Convierto cada texto en un conjunto de palabras

Busco las palabras en común

Busco todas las palabras sin repetir

Divido común / total

Si da más de 0.6 → son muy parecidos


Cojo los textos, quito palabras innecesarias, separo palabras, comparo cuáles se repiten y divido entre todas las que hay.
"""     


