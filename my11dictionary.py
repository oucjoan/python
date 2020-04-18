customer = {
    "name": "JoanZhang",
    "age": 20,
    "is_male": False
}
print(customer["name"])
#customer["birthdate"] = "Jan 1 1980"
print(customer.get("birthdate", "jan 1"))
print(customer.get("Name", "Lisa"))                     #大小写敏感
print(customer.get("work", "Engineer"))
print(customer["name"])
print(customer)

number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}

print(number.get("1", "two"))            # 如果有key1，则返回key的值，如果没有，返回two
phone = input("Phone: ")
output = ""
for ch in phone:
    output += number.get(ch, "*") + " "
print(output)

message = input(">")
words = message.split(' ')                 # 把字符串分成List
output2 = ""
emojis = {
    "morning": "早上",
    "night": "晚上"

}
for word in words:
    output2 += emojis.get(word, word) + " "
print(output2)
