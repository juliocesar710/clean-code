def maior(lista):
    maior = lista[0]

    for n in lista:
        if n > maior:
            maior = n

    return maior


valores = [12, 45, 7, 89, 23]

resultado = maior(valores)

print(resultado)