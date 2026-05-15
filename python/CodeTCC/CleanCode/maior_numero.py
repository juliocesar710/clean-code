def encontrar_maior_numero(lista_de_numeros):
    maior_numero_encontrado = lista_de_numeros[0]

    for numero_atual in lista_de_numeros:
        if numero_atual > maior_numero_encontrado:
            maior_numero_encontrado = numero_atual

    return maior_numero_encontrado


numeros_inteiros = [12, 45, 7, 89, 23]

maior_numero = encontrar_maior_numero(numeros_inteiros)

print(maior_numero)