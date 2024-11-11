class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._f = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            return None
        return self._data[self._f]
    
    def dequeue(self):
        if self.is_empty():
            return None
       
        answer = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % len(self._data)
        print("F value", self._f)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._f + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._f
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._f = 0
    
    def __str__(self):
        return "-".join(map(str, self._data))
    

queue = ArrayQueue()

for i in range(5):
    queue.dequeue()

for i in range(1, 12):
    queue.enqueue(i)

# queue.dequeue()
for i in range(1, 11):
    queue.dequeue()

print("Length of queue:", len(queue))
print(queue)