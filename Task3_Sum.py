class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(node):
    """
    Рекурсивна функція для знаходження суми всіх значень у двійковому дереві пошуку або AVL-дереві.

    :param node: корінь дерева, з якого починається обрахунок
    :return: сума всіх значень в дереві
    """
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад створення дерева і використання функції sum_of_values
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)

print("Сума всіх значень в дереві:", sum_of_values(root))
