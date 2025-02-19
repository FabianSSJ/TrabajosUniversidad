class Node:
    def _init_(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, root, key, priority):
        if not root:
            return Node(key, priority)
        if priority < root.priority:
            root.left = self.insert(root.left, key, priority)
        else:
            root.right = self.insert(root.right, key, priority)
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)
        
        if balance > 1 and priority < root.left.priority:
            return self.rotate_right(root)
        if balance < -1 and priority > root.right.priority:
            return self.rotate_left(root)
        if balance > 1 and priority > root.left.priority:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and priority < root.right.priority:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.priority = temp.priority
            root.right = self.delete(root.right, temp.key)
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)
        
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Paciente: {root.key}, Prioridad: {root.priority}")
            self.inorder(root.right)

# Ejemplo de uso
tree = AVLTree()
root = None
root = tree.insert(root, "Paciente1", 5)
root = tree.insert(root, "Paciente2", 2)
root = tree.insert(root, "Paciente3", 8)
root = tree.insert(root, "Paciente4", 1)
root = tree.insert(root, "Paciente5", 7)

tree.inorder(root)