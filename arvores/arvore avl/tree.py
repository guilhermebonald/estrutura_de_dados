""" 
Arvore AVL / Arvores Binárias de Busca Auto Balanceadas
"""


# Definindo a classe para um nó da árvore AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


# Função para calcular a altura de um nó
def height(node):
    if node is None:
        return 0
    return node.height


# Função para calcular o fator de balanceamento de um nó
def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


# Função para realizar a rotação simples à direita
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Realiza a rotação
    x.right = y
    y.left = T2

    # Atualiza as alturas
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# Função para realizar a rotação simples à esquerda
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Realiza a rotação
    y.left = x
    x.right = T2

    # Atualiza as alturas
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# Função principal para inserir um nó na árvore AVL
def insert(root, key):
    # Etapa 1: Inserção normal de um nó de árvore binária de busca
    if root is None:
        return Node(key)

    # if root is not none
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Chave já existe na árvore

    # Etapa 2: Atualiza a altura do nó atual
    root.height = 1 + max(height(root.left), height(root.right))

    # Etapa 3: Obtém o fator de balanceamento do nó e verifica se a árvore ficou desbalanceada
    balance = balance_factor(root)

    # Se o nó ficou desbalanceado, existem 4 casos possíveis

    # Caso da rotação à direita
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Caso da rotação à esquerda
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Caso da rotação à esquerda seguida de uma rotação à direita
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Caso da rotação à direita seguida de uma rotação à esquerda
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Função para percorrer a árvore AVL em ordem
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


def print_avl_tree(root, level=0):
    if root is not None:
        print_avl_tree(root.right, level + 1)
        print("    " * level + str(root.key))
        print_avl_tree(root.left, level + 1)


# Exemplo de uso
root = None
keys = [10, 20, 30, 15, 5]

# Inserindo chaves na árvore AVL
for key in keys:
    root = insert(root, key)

# Imprimindo a árvore em ordem
print("Árvore AVL em ordem:")
inorder_traversal(root)

print('\nArvore:')
print_avl_tree(root)