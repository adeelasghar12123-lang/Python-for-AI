from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return f"Queue: {list(self._items)}"


if __name__ == "__main__":
    my_queue = Queue()
    
    my_queue.enqueue("Alice")
    my_queue.enqueue("Bob")
    my_queue.enqueue("Charlie")
    
    print(my_queue)             
    print(my_queue.peek())      
    print(my_queue.dequeue())   
    print(my_queue)             
    print(my_queue.size())      
    print(my_queue.is_empty())  