def fact(n):
    # 正着加
    i = 1
    res = 1
    while i <= n:
        res = res * i
        i += 1
    return res

'''
    # 倒着减
    res = n
    while n > 0:
        res *= n
        n -= 1
'''

n = int(input('请输入数字：'))
print(fact(n))