class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.value:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.value:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def postOrder(self, root, result):
        if not root:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.value)

# Función para obtener la altura del árbol
    def getTreeHeight(self, root):
        if not root:
            return 0
        left_height = self.getTreeHeight(root.left)
        right_height = self.getTreeHeight(root.right)
        return 1 + max(left_height, right_height)


# Función para imprimir nodos en un nivel específico
    def printNodesAtLevel(self, root, level):

        if not root:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            left_count = self.printNodesAtLevel(root.left, level - 1)
            right_count = self.printNodesAtLevel(root.right, level - 1)
            return left_count + right_count


# Función para imprimir el árbol por niveles
    def printTreeByLevels(self, root):
        height = self.getTreeHeight(root)
        for level in range(1, height + 1):
            print(f"Nodos en el nivel {level}: ", end="")
            self.printNodesAtLevel(root, level)
            print()

tree = AVLTree()
C = int(input().strip())
n = 0
for _ in range(C):
    elements = input().strip().split()
    root = None
    for el in elements:
        if el == "-1":
            break
        root = tree.insert(root, el)
    heigth = tree.getTreeHeight(root)
    n = tree.printNodesAtLevel(root, heigth)
    print(n)
