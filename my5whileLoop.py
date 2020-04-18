i = 1
while i <= 3:
    print('#' * i)
    i += 1
print("done!")

right_number = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess_count += 1
    if int(input(f'Guess: ')) == right_number:
        print('You win!')
        break  # 跳出循环
else:
    print("You failed")

# 新练习程序
command = ""
started = False
while command.lower() != 'quit':
    command = input("> ").lower()
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
         """)
    elif command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Car started. Ready to go')
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == 'quit':
        break
    else:
        print("I don't understand that")

