def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresa un número: "))
resultado = suma_digitos(numero)
print("La suma de los dígitos es:", resultado)