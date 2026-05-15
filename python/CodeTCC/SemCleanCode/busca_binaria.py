def busca(lista, valor, inicio, fim):
    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio

        elif lista[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


numeros = [2, 5, 8, 12, 16, 23, 38, 45]

resultado1 = busca(numeros, 23, 0, len(numeros) - 1)
resultado2 = busca(numeros, 10, 0, len(numeros) - 1)

print(resultado1)
print(resultado2)