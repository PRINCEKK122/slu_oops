from empty_exception import Empty

class Node:
    __slots__ = "_element", "_next"
    
    def __init__(self, element, next):
        self._element = element
        self._next = next

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def insertHead(self, element):
        newNode = Node(element, self._head)
        self._head = newNode
        if self._tail is None:
            self._tail = self._head
        self._size += 1

    def insertTail(self, element):
        newNode = Node(element, None)
        if self._head is None:
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def removeHead(self):
        if self._head is None:
            raise Empty("Linked list is empty")
        
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            newHead = self._head._next
            self._head._next = None
            self._head = newHead
        self._size -= 1

    def removeTail(self):
        if len(self) == 0:
            raise Empty("Linked list is empty")

        if self._head == self._tail:
            self._head = self._tail = None
        else:
            currentElement = self._head
           
            while currentElement._next != self._tail:
                currentElement = currentElement._next
            newTail = currentElement
            currentElement._next = None
            self._tail = newTail
        self._size -= 1

    def __len__(self):
        return self._size

    def __str__(self):
        result = []
        currentNode = self._head
        while  currentNode is not None:
            result.append(currentNode._element)
            currentNode = currentNode._next
        
        return " -> ".join(map(str, result))

lst = SinglyLinkedList()
lst.insertHead(1)
lst.insertHead(2)
# lst.removeTail()
lst.insertTail(3)
lst.removeTail()
lst.removeTail()
# lst.insertHead(0)
# lst.insertTail(5)
# lst.removeHead()
# lst.removeHead()
# lst.removeHead()
# lst.removeHead()
# lst.removeHead()
print(lst)
print("Length", len(lst))