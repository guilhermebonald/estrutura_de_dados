class No:
    def __init__(self, valor, ponteiro=None):
        self.valor = valor
        self.ponteiro = ponteiro

    # Retorna a reprentação.
    def __repr__(self):
        return '%s -> %s' % (self.valor, self.ponteiro)


class ListaEncadeada:
    # Ponteiro da cabeça, para o inicio da lista. Endereço de memoria do primeiro Nó.
    def __init__(self):
        self.cabeca = None

    # Retorna a reprentação.
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"


# Inserção primeiro item da lista.
def insere_no_inicio(lista, novo_valor):
    # 1) Cria um novo nó com o valor fornecido (novo_valor).
    novo_no = No(novo_valor)

    # 2) Faz com que o ponteiro do novo nó aponte para o nó que era a cabeça da lista anteriormente.
    novo_no.ponteiro = lista.cabeca

    # 3) Atualiza a cabeça da lista para que ela aponte para o novo nó, tornando-o o novo nó da cabeça da lista.
    lista.cabeca = novo_no




lista = ListaEncadeada()
print("Lista vazia:", lista)

insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

insere_no_inicio(lista, 10)
print("Inserindo um novo elemento:", lista)
