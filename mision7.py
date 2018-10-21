def dividir(divisor, dividendo):
    numero1 = dividendo
    contador = 0
    while divisor & dividendo <= 0:
        if divisor <= 0:
            print("Por favor ingrese un numero que no sea menor o igual a 0")
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        contador = contador + 1
    print(numero1, "/", divisor, "=", contador, ", sobran ", dividendo)


def encontrarMayor():
    mayor = 0
    numero = 0
    while  numero != -1:
        numero = int(input("Dame un número [-1 para salir]: "))
        if numero == -1:
            continue
        if numero < -1:
            continue
        if numero > mayor:
            mayor = numero
        else:
            continue
    if not mayor == 0:
        print("El mayor es: ", mayor)
    else:
        print("No hay valor mayor")

def leerOpcion():
    print("Misión 07 Ciclos while")
    print("Autor: Danhel Alejandro Mercado")
    print("Matricula: A01329263")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Ingresa tu opción:"))
    return opcion


def main():
    opcion = leerOpcion()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Dame el dividendo: "))
            divisor = int(input("Dame el divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            print("Teclea una serie de números para encontrar el mayor.")
            encontrarMayor()
        elif opcion >= 0 or opcion < 3:
            print("Ingrese 1, 2 ó 3")
        opcion = leerOpcion()
    print("El programa ha terminado")

main()


