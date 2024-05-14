class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(node):
    """
    Функція для знаходження найменшого значення в двійковому дереві пошуку або AVL-дереві.

    :param node: корінь дерева, з якого починається пошук
    :return: найменше значення в дереві
    """
    current = node
    # йдемо до крайнього лівого вузла
    while current.left is not None:
        current = current.left
    return current.val

# Приклад створення дерева і використання функції find_min
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print("Найменше значення в дереві:", find_min(root))
