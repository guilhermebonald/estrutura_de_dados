""" 
Desafio: O desafio propõe implementar o método de caminhamento de ordem de nível transversal em Python, 
para resolver um problema de distribuição de ordens da matriz de uma empresa para suas filiais, seguindo 
uma estrutura de hierarquia. O desafio fornece um pseudocódigo da solução e pede para escrever a resposta 
no campo abaixo e anexar os arquivos.
"""


# Estrutura do nó da árvore
class Node:
    # função para criar um novo nó
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Função para imprimir a ordem de nível da árvore
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Imprimir nós em um determinado nível
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print("%d =>" % (root.data))
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


# Calcular a altura de uma árvore - o número de nós ao longo do caminho mais longo,
# do nó raiz até o o nó da folha mais distante
def height(node):
    if node is None:
        return 0
    else:
        # Calcular a altura de cada subárvore
        l_height = height(node.left)
        r_height = height(node.right)

        # Use o maior
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1


# Teste das funções
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Estrutura hierarquica da empresa")
printLevelOrder(root)
