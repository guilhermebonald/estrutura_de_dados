class No:
    def __init__(self, valor, ponteiro=None):
        self.valor = valor
        self.ponteiro = ponteiro

    # Retorna a reprentação.
    def __repr__(self):
        return "%s, %s" % (self.valor, self.ponteiro)


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

        # Percorre a lista até o último Nó ser vazio e adicionando +1 em cada loop.
        while atual is not None:
            tamanho += 1
            atual = atual.ponteiro

        return tamanho

    # Verifica se a lista está vazia.
    def lista_vazia(self, lista):
        if lista.cabeca == None:
            return True
        else:
            return False

    # Inserção primeiro item da lista.
    def insere_no_inicio(self, lista, novo_valor):
        # 1) Cria um novo nó com o valor fornecido (novo_valor).
        novo_no = No(novo_valor) # A classe Nó recebe um "valor" enquanto seu "ponteiro" por padrão já é None.

        # 2) Faz com que o ponteiro do novo nó aponte para o nó que era a cabeça da lista anteriormente.
        novo_no.ponteiro = lista.cabeca

        # 3) Atualiza a cabeça da lista para que ela aponte para o novo nó, tornando-o o novo nó da cabeça da lista.
        lista.cabeca = novo_no

    # inserção no último item da lista.
    def insere_no_fim(self, lista, no_anterior, novo_dado):
        assert no_anterior, "Nó anterior precisa existir na lista."

        # Cria um novo nodo com o dado desejado.
        novo_no = No(novo_dado)

        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_no.ponteiro = no_anterior.ponteiro

        # Faz com que o novo nodo seja o próximo do nodo anterior.
        no_anterior.ponteiro = novo_no



# Execução da Lista
lista = ListaEncadeada()

print(f"Lista vazia: {lista.lista_vazia(lista)}")
print(f"Tamanho da Lista: {lista.tamanho_lista()}")

lista.insere_no_inicio(lista, 5)
print("\nNovo elemento:", lista)
lista.insere_no_inicio(lista, 10)
print("Novo elemento:", lista)
lista.insere_no_inicio(lista, 15)
print("Novo elemento:", lista)

no_anterior = lista.cabeca
lista.insere_no_fim(lista, no_anterior, 20)
print(f"Novo elemento: {lista}")

print(f"\nLista vazia: {lista.lista_vazia(lista)}")
print(f"Tamanho da Lista: {lista.tamanho_lista()}")
