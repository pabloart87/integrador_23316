"""CALCULO DEL MAXIMO COMUN DIVISOR"""

def maximo_comun_divisor(n1, n2):
    a = n1
    b = n2
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return print(f"El MCD de {n1} y {n2} es: {a}")

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

maximo_comun_divisor(n1, n2)

# def get_int(n1):
#     if type(n1) == int:
#         print(f"el numero es correcto: {n1}" )
#     else:
#         print("el numero no es un entero, verifique")

# get_int(int(input("ingrese un entero por favor: ")))
    




