"""
A busca binária é uma técnica de pesquisa eficiente. Sua única restrição é 
que as chaves do conjunto de dados devem estar ordenadas. Logo, existe um 
custo inicial para armazenar os dados já ordenados ou executar um algoritmo 
de ordenação antes da busca binária. 

 a busca binária faz acessos à posição do meio do vetor comparando 
esse valor com a chave e, após, descartando uma das metades restantes. 
A cada iteração, o local de busca no vetor diminui pela metade, assim, tendo 
um bom desempenho.
"""

def binary_search(A, chave, N):
    esquerda = 0
    direita = N - 1
    while(esquerda <= direita):
        meio = int((esquerda + direita) / 2)
        if A[meio] < chave:
            return A[meio]
        elif A[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio + 1
    return 'Chave não encontrada'


lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(lista_num, 11, len(lista_num)))