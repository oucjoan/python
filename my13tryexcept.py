age =int(input('Age: '))
print(age)                      #如果输入是非整数，那么会出现valueerror


try:                                        #异常处理，将原来在终端报错的代码进行处理，使其他代码捕捉异常，避免代码崩溃
    age = int(input('Print Your Age: '))
    income = 200
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Wrong: Age cannot be 0.')
except ValueError:
    print('Wrong: Invalid value')