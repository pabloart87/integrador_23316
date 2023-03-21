"""CALCULO DE MINIMO COMUN MULTIPLO"""

def minimo_comun_multiplo(n1, n2):
    a = n1
    b = n2
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return print(f"El MCM de {n1} y {n2} es: {(n1 * n2) / a}")

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

minimo_comun_multiplo(n1, n2)

