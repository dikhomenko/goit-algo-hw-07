class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max(node):
    """
    Функція для знаходження найбільшого значення в двійковому дереві пошуку або AVL-дереві.

    :param node: корінь дерева, з якого починається пошук
    :return: найбільше значення в дереві
    """
    current = node
    # йдемо до крайнього правого вузла
    while current.right is not None:
        current = current.right
    return current.val

# Приклад створення дерева і використання функції find_max
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)

print("Найбільше значення в дереві:", find_max(root))
