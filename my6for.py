for item in [1, 2, 3, 'John', 'Smith']:
    print(item)
for item2 in range(90, 100, 3):  # range函数，第一个代表开始数字，中间代表结束数字，后面三个一间距，左闭右开，步长为3
    print(item2)

prices = [10, 20, 30]
Num = 0
for price in prices:
    Num += price
print(f"Total: {Num}")

for x in range(4):  # for循环嵌套
    for y in range(3):
        print(f'({x},{y})')

number = [1, 1, 1, 1, 5]
for star in number:
    output = ''
    for x_counter in range(star):
        output += 'x'
    print(output)



