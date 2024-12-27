class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

def evaluate_postfix(expression, stack_impl):
    stack = stack_impl()
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.push(a / b)
    
    return stack.pop()

def main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Usar Pila con Listas Enlazadas")
        print("2. Usar Pila con Arreglos")
        print("3. Evaluar Expresión en Notación Posfija")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            stack = LinkedListStack()
            stack_operations(stack)
        elif choice == '2':
            stack = ArrayStack()
            stack_operations(stack)
        elif choice == '3':
            expression = input("Ingrese una expresión en notación posfija (e.g., '3 4 + 2 *'): ")
            stack_choice = input("¿Usar (1) Listas Enlazadas o (2) Arreglos para la evaluación? ")
            stack_impl = LinkedListStack if stack_choice == '1' else ArrayStack
            try:
                result = evaluate_postfix(expression, stack_impl)
                print(f"Resultado: {result}")
            except Exception as e:
                print(f"Error evaluando la expresión: {e}")
        elif choice == '4':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def stack_operations(stack):
    while True:
        print("\n--- Operaciones de la Pila ---")
        print("1. Push (apilar)")
        print("2. Pop (desapilar)")
        print("3. Peek (consultar elemento superior)")
        print("4. Verificar si está vacía")
        print("5. Regresar al menú principal")
        choice = input("Seleccione una operación: ")

        if choice == '1':
            value = input("Ingrese un valor para apilar: ")
            stack.push(value)
            print(f"{value} ha sido apilado.")
        elif choice == '2':
            try:
                value = stack.pop()
                print(f"{value} ha sido desapilado.")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                value = stack.peek()
                print(f"Elemento superior: {value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '4':
            if stack.is_empty():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")
        elif choice == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
