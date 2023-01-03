class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = [None] *size


# my_stack = Stack(5)

    def is_empty(self):
        # if self.top == -1:
        #     return True
        # else:
        #     return False 아래와 같은 의미
        return True if (self.top == -1) else False

    def is_full(self):
        return True if (self.size -1 == self.top) else False

    def push(self, data):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.top += 1
            self.items[self.top] = data

    def pop(self):
        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.items[self.top]
            return value

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' +result
        return result # 왜 안될까 ㅠ

my_stack = Stack(5)

my_stack.push(1)
my_stack.push(2)
my_stack.pop()
my_stack.push(2)
my_stack.push(3)

print(my_stack)
print(my_stack.top)
print(my_stack.size)


print(my_stack)