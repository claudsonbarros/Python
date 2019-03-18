"""
Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições.
Crie uma função que recebe o vetor preenchido e substitua todas as ocorrências de valores negativos por zero,
as ocorrências de valores menores do que 10 por 1 e as demais ocorrências por 2.
"""

tam = 5

def troca(vetor,tam):
    for i in range(tam):
        if vetor[i] < 0:
            vetor[i] = 0
        elif vetor[i] > 0 and vetor[i] < 10:
            vetor[1] = 1
        else:
            vetor[i] = 2


v = [0]*tam
for i in range(tam):
    v[i] = int(input('Informe um valor Inteiro: '))


troca(v, tam)
print(v)

