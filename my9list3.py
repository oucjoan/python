numbers = [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9, 4, 0]
uniques = []
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)
