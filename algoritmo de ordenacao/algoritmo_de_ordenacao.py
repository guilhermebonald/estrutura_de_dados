# Ordenação por Inserção

def insertion_sort(lista, N):
    mudancas = 0
    # Começando do segundo elemento, pois sempre irá comparar aos numeros anteriores.
    for i in range(1, N):
        escolhido = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > escolhido:
            lista[j + 1] = lista[j]
            j = j - 1
            mudancas += 1
        lista[j + 1] = escolhido
    return mudancas

notas = [11, 4, 12, 45, 2]
mudancas = insertion_sort(notas, len(notas))
print(notas, mudancas)