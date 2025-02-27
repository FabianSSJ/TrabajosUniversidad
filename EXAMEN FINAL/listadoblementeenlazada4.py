class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  

class DoublyLinkedQueue:
    def __init__(self):
        self.front = None  
        self.rear = None  
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node 
        self.size += 1

    def dequeue(self):
        if not self.front:
            return None  
        value = self.front.value
        self.front = self.front.next  
        if self.front:  
            self.front.prev = None
        else: 
            self.rear = None
        self.size -= 1
        return value

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.front.value if self.front else None

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements

queue = DoublyLinkedQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Cola después de encolar:", queue.display())

print("Elemento desencolado:", queue.dequeue())
print("Cola después de desencolar:", queue.display())
