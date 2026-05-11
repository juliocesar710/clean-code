def calcular_media_de_tres(n1, n2, n3, proj=0):
    media = ((n1 + n2 + n3) / 3) + proj
    return media

def calcular_preenca(media, faltas):
    if(media>=7):
        if(faltas<=10):
            return "Aprovado"
        else:
            return "Reprovado por faltas"
    elif(media>=5):
        if(faltas<=10):
            return "Recuperação"
        else:
            return "Reprovado por faltas"
    else:
        return "Reprovado por média"


aluno1 = calcular_media_de_tres(7, 8, 9)
aluno2 = calcular_media_de_tres(5, 6, 7, proj=1)

print(calcular_preenca(aluno1, 8))
print(calcular_preenca(aluno2, 12))