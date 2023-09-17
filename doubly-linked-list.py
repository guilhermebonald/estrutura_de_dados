class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #* Para ficar mais facil de entender o que está acontecendo na hora de adicionar dados, seja no head ou no tail,
    #* é importante sempre ter em mente que os NÓS PRECISAM SEMPRE SE CONECTAR AO ANTERIOR E AO PROXIMO ATRAVEZ DO PONTEIRO.
    #? Tendo isso em mente ficará mais facil de compreender o que está acontecendo na hora de adicionar dados no inicio ou fim.
    def add_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # none[data]none
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_tail(self):
        # 1 - Encontre o último item da lista. Isso pode ser feito iterando pela lista até encontrar um nó cujo ponteiro next seja None.
        # 2 - Defina o ponteiro next do nó anterior ao último como None. Isso fará com que o último item da lista seja desconectado da lista.
        # 3 - Libere a memória do último item da lista. Isso pode ser feito usando o operador del.
        current = self.tail
        if self.head is None:
            print("Empty List")
        else:
            while current.next:
                current = current.next
            prev_node = current.prev
            prev_node.next = None    
            del current.data #! Problema ao excluir segundo item consecutivo 

    def delete_at_head(self):
        pass

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Execução
dll = DoublyLinkedList()
dll.add_at_head(2)
dll.add_at_head(3)
dll.add_at_tail(5)

dll.delete_at_tail()
dll.delete_at_tail()
dll.display_backward()