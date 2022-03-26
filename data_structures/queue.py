'''class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]

        return dequeue_object

    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]

        return peek_object

    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.front.data
            self.front = self.front.next

        if self.front is None:
            self.rear = None
        return  dequeue_object

    def peek(self):
        front_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            front_object = self.front.data
        return  front_object

    def isEmpty(self):
        is_empty = False
        if self.front is None:
            is_empty = True
        return is_empty