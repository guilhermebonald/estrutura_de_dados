class No:
    def __init__(self, valor, ponteiro=None):
        self.valor = valor
        self.ponteiro = ponteiro

    # Retorna a reprentação.
    def __repr__(self):
        return "%s -> %s" % (self.valor, self.ponteiro)


class ListaEncadeada:
    #  Inicializa a cabeça da lista como vazia, indicando que a lista está vazia no início.
    def __init__(self):
        self.cabeca = None

    # Retorna a reprentação.
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    # Metodo que informa o tamanho da lista
    def tamanho_lista(self):
        atual = self.cabeca
        tamanho = 0

        # verifica se a lista está vazia e retorna um 0
        if self.cabeca == None:
            return 0

        # Verifica se a lista possui somente um elemento
        if atual.conteudo != None and atual.proximo == None:
            return 1

        # Percorre a lista até o último Nó ser vazio e adicionando +1 em cada loop.
        while atual.proximo != None:
            tamanho = tamanho + 1
            atual = atual.proximo

        return tamanho

    # Inserção primeiro item da lista.
    def insere_no_inicio(self, lista, novo_valor):
        # 1) Cria um novo nó com o valor fornecido (novo_valor).
        novo_no = No(novo_valor)

        # 2) Faz com que o ponteiro do novo nó aponte para o nó que era a cabeça da lista anteriormente.
        novo_no.ponteiro = lista.cabeca

        # 3) Atualiza a cabeça da lista para que ela aponte para o novo nó, tornando-o o novo nó da cabeça da lista.
        lista.cabeca = novo_no


def lista_vazia(lista):
    if lista.cabeca == None:
        return True
    else:
        return False


# Execução da Lista
lista = ListaEncadeada()

print(lista_vazia(lista))

lista.insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

lista.insere_no_inicio(lista, 10)
print("Inserindo um novo elemento:", lista)

print(lista.tamanho_lista())

print(lista_vazia(lista))
