class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return f"Stack: {self._items}"


if __name__ == "__main__":
    my_stack = Stack()
    
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    

    
    print(my_stack)
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.size())
    print(my_stack.is_empty())