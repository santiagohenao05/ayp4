import re
texto="me gudta python, es genial. python es facil de aprender"
resultado=re.findall("python", texto)
print ("encontrado:", resultado)