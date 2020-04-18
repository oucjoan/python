names = ['Bob', 'Mary', 'Tom', 'Sarah', 'Mosh']
names[0] = 'BOB'
print(names[0])
print(names[2:])
print(names[2:4])

numbers = [3, 5, 8, 3, 5, 1, 90, 4, 7, 2, 6, 2, 6]
max_number = numbers[0]
for item in numbers:
    if item > max_number:
        max_number = item
print(max_number)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
for row in matrix:
    for colume in row:
        print(colume)


