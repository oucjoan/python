first = 'john'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)

print(len(msg))

print(msg.upper())
print(msg.lower())

# Find and replace method
print(msg.find('n'))  # 索引
print(msg.find('0'))   # 没有就返回-1
print(msg.find('Smith'))

print(msg.replace('coder', 'Computer Scientist'))  # 替换
print(msg.replace('c', 'C'))

print('Coder' in msg)           # in用于判断字符串的包含关系

print(msg.title())           # 每一个单词的第一个字母大写


