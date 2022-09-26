money = 50000
name = input('请输入您的姓名：')

def main_menu(name):
    print('---------------主菜单----------------')
    print(f'{name}，您好，欢迎来到银行ATM，请选择操作：\n查询余额 \t[输入1]\n存款 \t[输入2]\n取款 \t[输入3]\n退出 \t[输入4]\n')
    # num = input('请输入您的选择：')
    # if num == '1':
    #     query()
    # if num == '2':
    #     save_money()
    # if num == '3':
    #     minus_money()
    # else:
    #     print('已退出，欢迎下次光临！')

def query():
    print('---------------查询余额----------------')
    print(f'您当前的余额为{money}元')
    # main_menu(name)

def save_money():
    print('---------------存款----------------')
    change = float(input('请输入要存入的金额：'))
    global  money
    money += change
    print(f'当前余额为{money}元')
    # main_menu(name)

def minus_money():
    print('---------------取款----------------')
    change = float(input('请输入要存入的金额：'))
    global money
    money -= change
    print(f'当前余额为{money}元')
    # main_menu(name)

while True:
    main_menu(name)
    num = input('请输入您的选择：')
    if num == '1':
        query()
        continue
    elif num == '2':
        save_money()
        continue
    elif num == '3':
        minus_money()
        continue
    else:
        break


