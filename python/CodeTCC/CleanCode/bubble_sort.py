def trocar_posicoes(lista, indice_atual):
    lista[indice_atual], lista[indice_atual + 1] = (
        lista[indice_atual + 1],
        lista[indice_atual]
    )


def bubble_sort(lista_de_numeros):
    ultimo_indice = len(lista_de_numeros) - 1

    for indice_externo in range(ultimo_indice):

        for indice_atual in range(ultimo_indice - indice_externo):

            numero_atual = lista_de_numeros[indice_atual]
            proximo_numero = lista_de_numeros[indice_atual + 1]

            if numero_atual > proximo_numero:
                trocar_posicoes(lista_de_numeros, indice_atual)

    return lista_de_numeros


numeros_desordenados = [5, 2, 9, 1, 7]

numeros_ordenados = bubble_sort(numeros_desordenados)

print(numeros_ordenados)