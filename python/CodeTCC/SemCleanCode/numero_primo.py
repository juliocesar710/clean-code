def verificar_primo(num, inicio, fim, qtd_divisores):
    for i in range(inicio, fim + 1):
        if num % i == 0:
            qtd_divisores += 1

    if qtd_divisores == 2:
        return True
    else:
        return False


resultado1 = verificar_primo(7, 1, 7, 0)
resultado2 = verificar_primo(10, 1, 10, 0)

print(resultado1)
print(resultado2)