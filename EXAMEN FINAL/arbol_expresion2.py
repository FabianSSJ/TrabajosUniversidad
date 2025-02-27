class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in {"+", "-", "*", "/"}

def construct_tree(postfix):
    stack = []
    for char in postfix:
        if not is_operator(char):  # Si es un numero, crear un nodo hoja
            stack.append(Node(char))
        else:  # Si es un operador, crear nodo con dos hijos
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[-1]  # raiz del árbol

def evaluate(root):
    if root is None:
        return 0
    if not is_operator(root.value):  # Si es un numero, devolverlo
        return int(root.value)
    
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)
    
    if root.value == "+":
        return left_val + right_val
    elif root.value == "-":
        return left_val - right_val
    elif root.value == "*":
        return left_val * right_val
    elif root.value == "/":
        return left_val / right_val

postfix_expr = ["3", "5", "2", "8", "-", "*", "+"]  
root = construct_tree(postfix_expr)
print("Resultado:", evaluate(root)) 
