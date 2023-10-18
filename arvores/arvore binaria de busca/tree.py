"""
Arvore Binaria de Busca.
"""


class No(object):
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


class Arvore(object):
    def __init__(self):
        self.raiz = None
        self.cont_espaco = 10

    def inserir(self, chave: int) -> None:
        novo = No(chave)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if chave <= atual.chave:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

    def imprimir_arvore(self, raiz=None, espaco=0):
        if raiz == None:
            return
        espaco += self.cont_espaco

        self.imprimir_arvore(raiz.dir, espaco)

        print(end=" " * (espaco - self.cont_espaco))
        print(raiz.chave)

        self.imprimir_arvore(raiz.esq, espaco)


#Execution
lista = [115, 98, 34, 56, 25, 95, 25, 192, 130, 133]
arvore = Arvore()

for i in lista:
    arvore.inserir(i)

arvore.imprimir_arvore(arvore.raiz)