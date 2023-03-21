def contador_max(palabras):
    dic_frecuecia = {}
    for palabra in palabras:
        if palabra in dic_frecuecia:
            dic_frecuecia[palabra] += 1
        else:
            dic_frecuecia[palabra] = 1
    
    print(dic_frecuecia)
            
    p_max = max(dic_frecuecia.items())
    return tuple(p_max)

cadena = input("ingrese una cadena de caracteres para saber cual es el que mas se repite: ")
palabras = cadena.split()

print(contador_max(palabras))
