class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop desde la pila vacia")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Pila Vacia")
        return self.top.value

def is_balanced_parentheses(string):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.isEmpty() or stack.pop() != pairs[char]:
                return False

    return stack.isEmpty()

def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)

    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":

    test_string = "{[()]}"
    print(f"La cadena '{test_string}' esta balanceada: {is_balanced_parentheses(test_string)}")

    original_string = "Este es nuestro trabajo"
    print(f"cadena original: '{original_string}'")
    print(f"cadena revertida: '{reverse_string(original_string)}'")
