def eh_numero_primo(numero):
    if numero < 2:
        return False

    quantidade_divisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            quantidade_divisores += 1

    return quantidade_divisores == 2


numero_eh_primo = eh_numero_primo(7)
numero_eh_primo = eh_numero_primo(10)

print(numero_eh_primo)
print(numero_eh_primo)