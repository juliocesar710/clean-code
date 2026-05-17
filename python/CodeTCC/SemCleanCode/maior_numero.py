def maior(lista):
    maior = None

    for n in lista:

        if n > 0:

            if maior == None:
                    maior = n

            elif n > maior:
                    maior = n

    return maior


valores = [12, -4, 45, 18, 7, 89, 24]

resultado = maior(valores)

print(resultado)