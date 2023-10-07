# Ordenação por Inserção

"""
O Insertionsort, ou ordenação por inserção, é um algoritmo baseado em um 
jogo de cartas (ZIVIANI, 2004). Você está com um conjunto de cartas já 
ordenadas. Quando receber uma nova carta, deve colocá-la na posição correta, 
de forma que as cartas continuem ordenadas.

Exemplo: [6, 5, 3, 1, 8, 7, 2, 4]

Na primeira rodada, o escolhido é o 5. Vamos compará-lo com todos os 
elementos anteriores; nesse caso apenas o 6. Uma vez que o 5 é menor, vamos 
trocá-lo de posição. Na segunda rodada, o escolhido é o 3; vamos compará-lo 
com todos os anteriores, o 5 e o 6. Após as comparações, o 3 fica na primeira 
posição, e assim por diante.
"""

def insertion_sort(lista):
    mudancas = 0
    # Começando do segundo elemento, pois sempre irá comparar aos numeros anteriores.
    for i in range(1, len(lista)):
        # 5
        escolhido = lista[i]
        # Pegando o index do elemento anterior
        j = i - 1
        while j >= 0 and lista[j] > escolhido:
            lista[j + 1] = lista[j]
            j = j - 1
            mudancas += 1
        lista[j + 1] = escolhido
    return mudancas


# Não mudar os valores da lista, para não alterar o que foi documentado nos comentarios.
notas = [6, 5, 3, 1, 8, 7, 2, 4]
mudancas = insertion_sort(notas)
print(f"{notas}\nN° de mudanças: {mudancas}")
