import  random

num_base = random.randint(1,11)
num_user = eval(input('请输入1~10的整数：'))
'''
if num_base == num_user:
    print('猜对了')
elif num_base < num_user:
    print('猜大了，再一次：')
    num_user = eval(input('请输入：'))
    if num_base == num_user:
        print('猜对了')
    else:
        print('GAME OVER')
else:
    print('猜小了，再来一次：')
    num_user = eval(input('请输入：'))
    if num_base == num_user:
        print('猜对了')
    else:
        print('GAME OVER')
'''
i = 0
while num_base != num_user:
    i += 1
    print('猜错了，再来一次：')
    num_user = eval(input('请输入数字：'))

print(f'猜对了，共用{i}次，数字是{num_base}')