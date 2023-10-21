"""
Arvore Binaria de Busca.
"""


# Definindo a classe No
class No(object):
    # Construtor da classe No
    def __init__(self, chave):
        self.chave = chave  # A chave do nó
        self.esq = None  # O nó filho à esquerda
        self.dir = None  # O nó filho à direita


# Definindo a classe Arvore
class Arvore(object):
    # Construtor da classe Arvore
    def __init__(self):
        self.raiz = None  # A raiz da árvore
        self.cont_espaco = 10  # Contador de espaços para impressão da árvore

    # Método para inserir um nó na árvore
    def inserir(self, chave: int) -> None:
        novo = No(chave)  # Cria um novo nó
        if self.raiz == None:  # Se a árvore estiver vazia
            self.raiz = novo  # O novo nó se torna a raiz
        else:  # Se a árvore não estiver vazia
            atual = self.raiz  # Começa pela raiz
            while True:  # Loop infinito até encontrar onde inserir o novo nó
                anterior = atual
                if (
                    chave <= atual.chave
                ):  # Se a chave for menor ou igual à chave do nó atual
                    atual = atual.esq  # Vai para o nó à esquerda
                    if atual == None:  # Se não houver nó à esquerda
                        anterior.esq = novo  # Insere o novo nó à esquerda
                        return
                else:  # Se a chave for maior que a chave do nó atual
                    atual = atual.dir  # Vai para o nó à direita
                    if atual == None:  # Se não houver nó à direita
                        anterior.dir = novo  # Insere o novo nó à direita
                        return

        # Método para remover um nó da árvore

    def remover(self, chave: int) -> None:
        # Chama a função auxiliar _remover
        self.raiz = self._remover(self.raiz, chave)

    # Função auxiliar para remover um nó
    def _remover(self, raiz: No, chave: int) -> No:
        # Se a raiz é None, então a árvore está vazia
        if raiz is None:
            return raiz

        # Se a chave a ser removida é menor que a chave da raiz,
        # então ela está na subárvore à esquerda
        if chave < raiz.chave:
            raiz.esq = self._remover(raiz.esq, chave)
        # Se a chave a ser removida é maior que a chave da raiz,
        # então ela está na subárvore à direita
        elif chave > raiz.chave:
            raiz.dir = self._remover(raiz.dir, chave)
        else:
            # Se a chave é igual à chave da raiz, então este é o nó
            # a ser removido

            # Nó com apenas um filho ou sem filhos
            if raiz.esq is None:
                temp = raiz.dir
                raiz = None
                return temp
            elif raiz.dir is None:
                temp = raiz.esq
                raiz = None
                return temp

            # Nó com dois filhos: Obtém o sucessor in-order (menor na subárvore à direita)
            temp = self.minValorNo(raiz.dir)

            # Copia o conteúdo do sucessor in-order para este nó
            raiz.chave = temp.chave

            # Remove o sucessor in-order
            raiz.dir = self._remover(raiz.dir, temp.chave)

        return raiz

    # Função para encontrar o nó com menor valor (usada em _remover)
    def minValorNo(self, no: No) -> No:
        current = no

        # Percorre a árvore para encontrar o filho mais à esquerda
        while current.esq is not None:
            current = current.esq

        return current

    # Imprimir
    def imprimir_arvore(self, raiz=None, espaco=0):
        if raiz == None:
            return
        espaco += self.cont_espaco

        self.imprimir_arvore(raiz.dir, espaco)

        print(end=" " * (espaco - self.cont_espaco))
        print(raiz.chave)

        self.imprimir_arvore(raiz.esq, espaco)


# Execution
lista = [115, 98, 34, 56, 25, 95, 25, 192, 130, 133]
arvore = Arvore()

for i in lista:
    arvore.inserir(i)

arvore.imprimir_arvore(arvore.raiz)

arvore.remover(192)

arvore.imprimir_arvore(arvore.raiz)
