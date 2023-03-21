def dicFrecuencia(palabras):
    dic_frecuecia = {}
    for palabra in palabras:
        if palabra in dic_frecuecia:
            dic_frecuecia[palabra] += 1
        else:
            dic_frecuecia[palabra] = 1
            
    print(dic_frecuecia)
    
    for palabra in dic_frecuecia:
        frecuencia = dic_frecuecia[palabra]
        print(f"La palabra {palabra} tiene una frecuencia de {frecuencia}")
    return dic_frecuecia

cadena = input("ingrese una cadena de caracteres: ")
palabras = cadena.split()

dicFrecuencia(palabras)