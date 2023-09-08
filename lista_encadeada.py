# Definindo a classe Node
class Node:
    # O construtor recebe o valor e o próximo nó como parâmetros
    def __init__(self, value, next=None):
        self.value = value # Atribuindo o valor ao atributo value
        self.next = next # Atribuindo o próximo nó ao atributo next

# Definindo a classe LinkedList
class LinkedList:
    # O construtor recebe a cabeça da lista como parâmetro
    def __init__(self, head=None):
        self.head = head # Atribuindo a cabeça ao atributo head

    # Método para inserir um elemento no início da lista
    def insert_at_head(self, value):
        # Criando um novo nó com o valor dado e o atual head como próximo
        new_node = Node(value, self.head)
        # Atualizando o head para ser o novo nó
        self.head = new_node

    # Método para inserir um elemento no final da lista
    def insert_at_tail(self, value):
        # Criando um novo nó com o valor dado e sem próximo
        new_node = Node(value)
        # Verificando se a lista está vazia
        if self.head is None:
            # Se sim, o head é o novo nó
            self.head = new_node
        else:
            # Se não, percorrendo a lista até chegar no último nó
            current = self.head
            while current.next is not None:
                current = current.next
            # Fazendo o último nó apontar para o novo nó
            current.next = new_node

    # Método para remover um elemento do início da lista
    def remove_from_head(self):
        # Verificando se a lista está vazia
        if self.head is None:
            # Se sim, não há nada para remover
            return None
        else:
            # Se não, guardando o valor do head em uma variável
            value = self.head.value
            # Atualizando o head para ser o próximo nó
            self.head = self.head.next
            # Retornando o valor removido
            return value

    # Método para remover um elemento do final da lista
    def remove_from_tail(self):
        # Verificando se a lista está vazia
        if self.head is None:
            # Se sim, não há nada para remover
            return None
        else:
            # Se não, percorrendo a lista até chegar no penúltimo nó
            previous = None
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            # Guardando o valor do último nó em uma variável
            value = current.value
            # Verificando se a lista tem apenas um elemento
            if previous is None:
                # Se sim, o head é None
                self.head = None
            else:
                # Se não, fazendo o penúltimo nó apontar para None
                previous.next = None
            # Retornando o valor removido
            return value

    # Método para imprimir os elementos da lista na tela
    def print_list(self):
        # Inicializando uma variável para armazenar a representação da lista
        output = ""
        # Percorrendo a lista e adicionando os valores à variável
        current = self.head
        while current is not None:
            output += str(current.value) + " -> "
            current = current.next
        # Adicionando o símbolo de fim de lista
        output += "None"
        # Imprimindo a variável na tela
        print(output)


lista = LinkedList()

lista.print_list()
lista.insert_at_head(5)
lista.insert_at_head(10)
lista.insert_at_tail(15)
lista.print_list()