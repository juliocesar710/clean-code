NOTA_MINIMA_APROVACAO = 7
NOTA_MINIMA_RECUPERACAO = 5
MAX_FALTAS = 10


def calcular_media(nota1, nota2, nota3, bonus=0):
    media_base = (nota1 + nota2 + nota3) / 3
    return media_base + bonus


def verificar_situacao(media_final, quantidade_faltas):
    if quantidade_faltas > MAX_FALTAS:
        return "Reprovado por faltas"

    if media_final >= NOTA_MINIMA_APROVACAO:
        return "Aprovado"

    if media_final >= NOTA_MINIMA_RECUPERACAO:
        return "Recuperação"

    return "Reprovado por média"

aluno1_media = calcular_media(7, 8, 9)
aluno2_media = calcular_media(5, 6, 7, bonus=1)

faltas_aluno1 = 8
faltas_aluno2 = 12

print(verificar_situacao(aluno1_media, faltas_aluno1))
print(verificar_situacao(aluno2_media, faltas_aluno2))