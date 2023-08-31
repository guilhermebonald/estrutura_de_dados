class No:
    def __init__(self, valor, ponteiro=None):
        self.valor = valor
        self.ponteiro = ponteiro


class ListaEncadeada:
    # TODO - Ponteiro da cabeça, para o inicio da lista. Endereço de memoria do primeiro Nó.
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    # TODO -  Retorna a reprentação da Lista em memoria.
    def __repr__(self):
        return str(self.cabeca)

    # TODO - Inserção primeiro item da lista.
    def inserir_inicio(self, lista, novo_valor):
        # ? - Cria um novo "no" com o "valor" a ser armazenado
        novo_no = No(novo_valor)

        # ? Fazer o ponteiro do novo nó apontar para o atual nó cabeça da lista.
        novo_no.ponteiro = lista.cabeca

        # ? Faz com que a "cabeca" referencie o novo "no"
        lista.cabeca = novo_no


lista = ListaEncadeada()
ListaEncadeada().inserir_inicio(lista=lista, novo_valor=10)
ListaEncadeada().inserir_inicio(lista=lista, novo_valor=5)
print(lista)
