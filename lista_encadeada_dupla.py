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
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Execução
dll = DoublyLinkedList()
dll.add_at_head(2)
dll.add_at_head(3)
dll.add_at_tail(5)

dll.display_backward()
dll.display_forward()
