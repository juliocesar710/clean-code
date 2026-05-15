def buscar_valor(lista_ordenada, valor_procurado):
    indice_inicial = 0
    indice_final = len(lista_ordenada) - 1

    while indice_inicial <= indice_final:
        indice_meio = (indice_inicial + indice_final) // 2

        valor_atual = lista_ordenada[indice_meio]

        if valor_atual == valor_procurado:
            return indice_meio

        if valor_atual < valor_procurado:
            indice_inicial = indice_meio + 1
        else:
            indice_final = indice_meio - 1

    return -1


numeros_ordenados = [2, 5, 8, 12, 16, 23, 38, 45]

posicao_numero_23 = buscar_valor(numeros_ordenados, 23)
posicao_numero_10 = buscar_valor(numeros_ordenados, 10)

print(posicao_numero_23)
print(posicao_numero_10)