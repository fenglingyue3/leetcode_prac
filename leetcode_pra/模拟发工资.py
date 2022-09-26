import  random

money = 10000
for i in range(1,21):
    if (money-1000)>=0:
        rank = random.randint(1, 10)
        if rank >= 5:
            money -= 1000
            print(f'{i}号已发工资1000。')
        else:
            print(f'{i}号绩效未达标。')
            continue
    else:
        print(f'余额不足还剩{money}元')

print('本月额度已用完。')

