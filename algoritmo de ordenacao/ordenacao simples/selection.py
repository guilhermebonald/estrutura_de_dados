# Ordenação por Seleção

"""
O Selectionsort, ou ordenação por seleção, é um algoritmo que busca o menor 
elemento (ou o maior depende do tipo de ordenação que está sendo feita) de 
cada iteração e o coloca na sua posição correta.

Dado um vetor ou uma lista de elementos que desejamos ordenar, esse 
algoritmo irá buscar na primeira iteração o menor elemento de todos e colocá-lo 
na primeira posição do vetor. Na segunda iteração, ele buscará pelo segundo 
menor e o colocará na posição dois, e assim sucessivamente.
"""


def selection_sort(lista):
    n = len(lista)
    # Primeiro começamos descobrindo o valor minimo da lista e pegando seu index
    for i in range(n - 1): # Não precisamos percorrer até o ultimo elemento.
        min_index = i  # Index minimo porque ele sempre vai percorrer a sub-lista [28, {44, (35, 12, 55, 85, 31, 96]
        # Pega o VALOR minimo da lista
        for j in range(min_index, n): 
            if lista[j] < lista[min_index]:  
                min_index = j
        # Troca os valores de posição
        if lista[i] > lista[min_index]:
            aux = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = aux


numeros = [28, 44, 35, 12, 55, 85, 31, 96]

selection_sort(numeros)
print(numeros)
