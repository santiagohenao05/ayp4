"""import re
match: #buscar al inicio
search: #buscar en cualqueir parte 
findall: #busca una palabra
reglas: antes - ? 0/1 veces
* 0/n veces
+ 1/n veces"""
import re
texto="ac abc abbc abbbc abbbbc"
resultado=re.findall(r"a[bd]{2,3}c", texto)
print(f"abc (cero o mas b): {resultado}")


