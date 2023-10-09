# Ordenação por bolha

"""
O Bubblesort, ou ordenação por bolha, como é popularmente conhecido, leva 
esse nome, pois sua estrutura foi pensada como se os elementos maiores do 
vetor desordenado fossem mais leves e flutuassem como bolhas até as suas 
posições corretas.

Dado um vetor ou uma lista de elementos que desejamos ordenar, comparamos 
os elementos dois a dois até que o vetor esteja completamente ordenado. 
Por exemplo, em um vetor de cinco elementos, vamos comparar o 1º 
elemento com o 2º, o 2º com o 3º, e assim sucessivamente. Essas operações 
são repetidas até que nenhuma troca de elementos ocorra, o que indica que 
o vetor está ordenado
"""

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

numeros = [28, 44, 35, 12, 55, 85, 31, 96]

bubble_sort(numeros)
print(numeros)