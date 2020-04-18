is_goodcredit = True
price = 1000000

if is_goodcredit:
    payment = 0.9 * price
else:
    payment = 0.8 * price
print(f'The price of the house is ${payment}')

has_good_credit = True
has_high_income = False
has_crimal_records = True
if (has_good_credit or has_high_income) and not has_crimal_records:
    print('Eligible loan')
else:
    print('uneligible loan')

temperature = 35  # int(input("Pleare type the current temperature: "))
if temperature > 30:  # < > >= <= == !=
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a warm day")

name = 'hsthfgbgffhkhfhhdrtrthsdhstrhtrhstrherttr'
if len(name) < 3:
    print('Wrong: name must be at least 3 characters.')
elif len(name) > 50:
    print('Wrong: name can be a maximum of 50 characters.')
else:
    print('You got a proper name!')

weight = float(input('weight: '))

unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"you are {converted} kilos.")
elif unit.lower() == 'k':
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
else:
    print("Wrong!")
