def sumList(lst):
    if len(lst) == 1:
        return lst[0]
    
    return lst[0] + sumList(lst[1:])


def reverseOrder(lst):
    if len(lst) > 0:
        print(lst[-1], end = " ")
        reverseOrder(lst[:-1])
    


# reverseOrder([1, 2, 3, 4, 5])
print(sumList([1, 2, 3]))