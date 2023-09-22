"""
Esse desafio precisa verificar a quantidade de produtos na lista que precisa de refrigeração.
Na lista deve conter produtos de "Peso 0 = enlatados" e "Peso 1 = refrigerados.
"""


class Produto:
    def __init__(self, nome: str, peso: int):
        # Peso 0 = enlatados : Peso 1 = Refrigerados
        self.nome = nome
        self.peso = peso


class No:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

    def __str__(self):
        return "%s -> %s" % (self.value, self.pointer)


class ListaProduto:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def head_append(self, value):
        # Criação do Nó
        node = No(value)
        # Ponteiro recebe a cabeça para apontar o dado
        node.pointer = self.head
        # head recebe o Nó completo com valor e ponteiro
        self.head = node

    def total_produto_refrigerado(self):
        atual = self.head
        count_enlatados = 0
        count_refrigerados = 0

        if self.head == None:
            print("Empty List")
        else:
            while atual:
                peso = atual.value.peso
                if peso == 0:
                    count_enlatados += 1
                elif peso == 1:
                    count_refrigerados += 1
                atual = atual.pointer

            print(f"Enlatados: {count_enlatados}")
            print(f"Refrigerados: {count_refrigerados}")


# Execução

lista = ListaProduto()
lista.head_append(Produto(nome='Alcatra', peso=1))
lista.head_append(Produto(nome='Sardinha', peso=0))
lista.head_append(Produto(nome='Patinho', peso=1))
lista.head_append(Produto(nome='Refrigerante', peso=1))

lista.total_produto_refrigerado()