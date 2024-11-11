from empty_exception import Empty

class ArrayStack:
    """LIFO stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.__data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.__data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self.__data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.__data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")

        return self.__data[-1]

    def pop(self):
        """Remove and return the element from teh top of the stack (i.e., LIFO)
        
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            # raise Empty("Stack is empty")
            return None
        return self.__data.pop()

    def __str__(self):
        return "->".join(map(str, self.__data))
    
def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise"""
    lefty = "({["
    righty = ")}]"

    stack = ArrayStack()

    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()


S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)

T = ArrayStack()
T.push(4)
T.push(10)

def transfer(S, T):
   while not S.is_empty():
       T.push(S.pop())
transfer(S, T)
print(len(S))
print("T stack", T)


def removeElementsFromStack(stack):
    if len(stack) <= 0:
        return
    print(stack)
    stack.pop()
    return removeElementsFromStack(stack)

def reverseNumbers(numbers):
    s = ArrayStack()
    
    iterator = range(len(numbers) - 1, -1, -1)
    
    for i in iterator:
        s.push(numbers[i])

    for i in iterator:
        numbers[i] = s.pop()
   
numbers = [100, 1, 2, -3, 4]
print("Original numbers", numbers)
reverseNumbers(numbers)
print("Reverse", numbers)
S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
S.push(-1)
# print("Top of S stack", S.top())
removeElementsFromStack(S)

# T = ArrayStack()
# T.push(10)

# transfer(S, T)
# print("S stack", S)
# print("T stack", T)
