"""
Arvore Binaria >>> Arvore Binaria de Busca
"""

class No:
    def __init__(self, item):
        self.item = item
        self.esq = None
        self.dir = None

def inOrdem(raiz, inorder):
    if raiz is None:
        return
    inOrdem(raiz.esq, inorder)
    inorder.append(raiz.item)
    inOrdem(raiz.dir, inorder)

def contaNo(raiz):
    if raiz is None:
        return 0
    return contaNo(raiz.esq) + contaNo(raiz.dir) + 1

def arrayToBst(arr, raiz):
    if raiz is None:
        return
    arrayToBst(arr, raiz.esq)
    raiz.item = arr[0]
    arr.pop(0)
    arrayToBst(arr, raiz.dir)

def converte(raiz):
    if raiz is None:
        return
    n = contaNo(raiz)
    arr = [0]
    inOrdem(raiz, arr)
    arr.sort()

def imprimir_arvore(raiz, espaco = 0):
    cont_espaco = 10
    if (raiz == None):
        return
    
    espaco += cont_espaco

    imprimir_arvore(raiz.dir, espaco)

    print(end= " "*(espaco - cont_espaco))
    print(raiz.item)
    
    imprimir_arvore(raiz.esq, espaco)


raiz = No(10)
raiz.esq = No(2)
raiz.dir = No(7)
raiz.esq.esq = No(8)
raiz.esq.dir = No(4)

converte(raiz)

imprimir_arvore(raiz)