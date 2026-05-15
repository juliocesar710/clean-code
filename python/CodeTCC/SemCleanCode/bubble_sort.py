def ordenar(lista):
    for i in range(len(lista)):

        for j in range(len(lista) - 1):

            if lista[j] > lista[j + 1]:

                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

    return lista


numeros = [5, 2, 9, 1, 7]

resultado = ordenar(numeros)

print(resultado)