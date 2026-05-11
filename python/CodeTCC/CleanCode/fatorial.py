def calcular_fatorial(numero):
    fatorial = 1

    for multiplicador in range(1, numero + 1):
        fatorial *= multiplicador

    return fatorial


fatorial_de_5 = calcular_fatorial(5)
fatorial_de_3 = calcular_fatorial(3)

print(fatorial_de_5)
print(fatorial_de_3)