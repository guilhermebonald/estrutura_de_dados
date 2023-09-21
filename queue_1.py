# Nó para alocação de uma Fila
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Classe que define uma Fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # inserir na fila
    def append(self, data):
        """Insere um elemento na fila"""
        node = Node(data)
        if self.first is None:
            self.first = self.last = node
        else:
            self.last.next = node # o ultimo dado da lista deve apontar para o novo Nó que estamos inserindo para ligar o agora penultimo ao ultimo.
            self.last = node # o ultimo da lista agora passa a ser o novo Nó adicionado.
            
        self._size += 1

    # remover da fila
    def pop(self):
        """Remove o elemento do topo da pilha""" 
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            # faltou tratar este caso no vídeo #
            if self.first is None:
                self.last = None
            ####################################
            self._size = self._size - 1
            return elem
        
        raise IndexError("The queue is empty")

    # observar o primeiro da fila
    def peek(self):
        """Retorna o topo sem remover"""
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()
    

queue = Queue()

queue.append("Klebin")
queue.append("Faker")
queue.append("João")

print(len(queue))

print(queue)