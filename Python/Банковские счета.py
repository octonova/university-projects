def deposit(x):
    name, money = x
    functionBank[name] = functionBank.setdefault(name, 0) + int(money)


def withdraw(x):
    name, money = x
    functionBank[name] = functionBank.setdefault(name, 0) - int(money)


def balance(x):
    name = x[0]
    if name in functionBank:
        print(functionBank[name])
    else:
        print('ERROR')


def transfer(x):
    name_1, name_2, money = x
    for name in (name_1, name_2):
        if name not in functionBank:
            deposit((name,0))
    withdraw((name_1, money))
    deposit((name_2, money))


def income(x):
    percent = int(x[0])
    for name, balanse in functionBank.items():
        if balanse > 0:
            functionBank[name] = functionBank.get(name) + balanse * percent // 100


try:
    functionBank = {}
    bank_fun = {'DEPOSIT': deposit, 'WITHDRAW': withdraw, 'BALANCE': balance, 'TRANSFER': transfer, 'INCOME': income}
    while 1:
        data = input().split()
        fun_name = data[0]
        arg = data[1:]
        bank_fun[fun_name](arg)
except EOFError:
    print("ERROR")
except SyntaxError:
    print("Invalid Data!")