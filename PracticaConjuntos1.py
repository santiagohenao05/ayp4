"""Enunciado: Análisis de amigos en una red social

Una red social quiere desarrollar un programa en Python para analizar las amistades entre usuarios.

Se tienen tres usuarios principales, y cada uno tiene una lista de amigos:

Amigos de Ana
Amigos de Luis
Amigos de Carlos

Estas colecciones deben manejarse mediante conjuntos de Python o, si se desea, mediante listas ligadas.

El programa debe permitir:
Mostrar todos los amigos registrados entre los tres usuarios.
Mostrar los amigos en común entre Ana y Luis.
Mostrar los amigos que tiene Carlos y no tiene Ana.
Mostrar los amigos que están conectados con al menos uno de los usuarios.
Verificar si una persona específica es amiga de un usuario determinado.
Agregar un nuevo amigo a un usuario.
Eliminar un amigo de un usuario.
Contar cuántos amigos tiene cada usuario."""

amigos_Ana={"Luis", "Carlos", "María", "Sofía"}
amigos_Luis={"Ana", "Carlos", "Pedro", "Sofía"}
amigos_Carlos={"Ana", "Luis", "María", "Juan"}

#mostrar todos los amigos registrados entre los tres usuarios
todos_amigos=amigos_Ana | amigos_Luis | amigos_Carlos
print("Todos los amigos registrados entre los tres usuarios:", todos_amigos)
#mostrar los amigos en común entre Ana y Luis
amigos_comunes_Ana_Luis=amigos_Ana & amigos_Luis
print("Amigos en común entre Ana y Luis:", amigos_comunes_Ana_Luis)
#mostrar los amigos que tiene Carlos y no tiene Ana
amigos_Carlos_no_Ana=amigos_Carlos - amigos_Ana
print("Amigos que tiene Carlos y no tiene Ana:", amigos_Carlos_no_Ana)
#mostrar los amigos que están conectados con al menos uno de los usuarios
amigos_conectados=amigos_Ana | amigos_Luis | amigos_Carlos
print("Amigos conectados con al menos uno de los usuarios:", amigos_conectados)
#verificar si una persona específica es amiga de un usuario determinado
persona="María"
usuario="Ana"   
if persona in amigos_Ana:
    print(f"{persona} es amiga de {usuario}.")
else:    print(f"{persona} no es amiga de {usuario}.")
#agregar un nuevo amigo a un usuario        
nuevo_amigo="Santiago"
amigos_Ana.add(nuevo_amigo)
print(f"Amigos de {usuario} después de agregar a {nuevo_amigo}:", amigos_Ana)
#eliminar un amigo de un usuario
amigo_a_eliminar="Sofía"
amigos_Luis.discard(amigo_a_eliminar)
print(f"Amigos de {usuario} después de eliminar a {amigo_a_eliminar}:", amigos_Luis)