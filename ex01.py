def encontrar_valores_repetidos(a, b):

    conjunto_a = set(a)
    
    repetidos = []
    
    for valor in b:

        if valor in conjunto_a and valor not in repetidos:
            repetidos.append(valor)
    
    return repetidos


#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#b = [4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
#resultado = encontrar_valores_repetidos(a, b)
#print(resultado)
