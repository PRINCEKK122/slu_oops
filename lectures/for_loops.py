# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(number)

# myList = [1, 2, 3, 4,5,6,7,8,9,10]
# for number in myList:
#     print(number)

# groceries = ['milk', 'eggs', 'bread', 'ham']
# count = 0
# for item in groceries:
#     count = count + 1
#     print(str(count) + ". " + item)

# for chapter in ('1', '2'):
#     print('Chapter ' + chapter)
#     for section in ('a', 'b', 'c'):
#         print('Section ' + chapter + section)
# print('Appendix')

original = ['A', 'B', 'C', 'D', 'E', 'F']
for letter in original:
    print(letter)

for i, letter in enumerate(original):
    print(i, letter)
    original.remove(letter)
    original.append(letter)
    print(original)

print(original)