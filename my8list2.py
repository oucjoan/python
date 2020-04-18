numbers = [24, 51, 89, 34, 55, 38, 31, 39, 55]
numbers2 = numbers.copy()               # 复制列表
numbers.append(40)                      # 在后面增加一个数
numbers.insert(0, 99)                   # 在索引位置插入一个数
numbers.remove(24)                      # 移除某个数
#numbers.clear()                        # 清空列表
numbers.pop()                           # 在末尾删除一个数字
print(numbers.index(34))                # 索引
#print(numbers.index(88))               # 不存在，会提示错误
print(88 in numbers)                    # 表达式，输出True or False
print(numbers.count(55))                # 列表中的元素数量
print(numbers)

numbers2.sort()                          # 排序
print(numbers2)
numbers2.reverse()
print(numbers2)
