"""dos conjuntos de canciones que le gustan a juan y a maria. Cuales son las acanciones que ambos les gustan?"""
from conjuntos2 import Conjunto


canciones_juan={
    "Tuki tuki", "aceite de coco","vvs1", "little demon","diomedez"
}
canciones_maria={
    "diomedez", "EMHDM", "tuki tuki", "Los cacorros usan kleimond", "little demon"
}
compartidas=canciones_juan.intersection(canciones_maria)
print (compartidas)

canciones_juan_clases=Conjunto(["Tuki tuki", "aceite de coco","vvs1", "little demon","diomedez"])
canciones_maria_clases=Conjunto(["diomedez", "EMHDM", "tuki tuki", "Los cacorros usan kleimond", "little demon"])

compartidas_clases=canciones_juan_clases.interseccion(canciones_maria_clases)
print (compartidas)
print(compartidas_clases)
#que recomendaciones de canciones le puede dar a juan?
recomendaciones_juan=canciones_maria-canciones_juan
print (recomendaciones_juan)
#todo el catalogo de canciones
catalogo=canciones_juan.union(canciones_maria)
print (catalogo)
