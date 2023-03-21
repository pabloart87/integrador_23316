def get_int(edad):
    try:
        if int(edad) >= 0:
            return print(f"Ingresó correctamente su edad: {edad}")
        else:
            return print("ingrese numeros positivos!") 
    except ValueError:
        edad = ""
        return print("ingrese valores numericos")

edad = (input("ingrese su edad: "))
get_int(edad)
