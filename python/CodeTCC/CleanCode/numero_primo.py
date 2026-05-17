def eh_numero_primo(numero):
    if numero < 2:
        return False

    quantidade_divisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            quantidade_divisores += 1

    return quantidade_divisores == 2


resultado_1 = eh_numero_primo(7)
resultado_2 = eh_numero_primo(10)

print(resultado_1)
print(resultado_2)