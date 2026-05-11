def verificar_primo(num):
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        return True
    else:
        return False


resultado1 = verificar_primo(7)
resultado2 = verificar_primo(10)

print(resultado1)
print(resultado2)