def calcular_fatorial(num):
    resultado = 1

    for i in range(1, num + 1):
        resultado = resultado * i

    return resultado


valor1 = calcular_fatorial(5)
valor2 = calcular_fatorial(3)

print(valor1)
print(valor2)