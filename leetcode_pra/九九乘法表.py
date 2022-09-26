# 1.需要有一个变量控制行 i<=9
# 2.需要有一个变量控制列 j<=i
# 3.每行输出的内容 列 * 行 j*i
'''
i = 1
while i <= 9:
    j = 1
    while j <=i:
        print(f'{j}*{i}={j*i}\t',end='')
        j +=1
    print('') #控制外层换行
    i += 1
'''
'''
name = 'itheima is abrand of itcast'
count = 0
for i in name:
    if i == 'a':
        count +=1
print(f'name中有{count}个a')
'''
'''
num = int(input('请输入自然数:'))
count = 0
for x in range(num+1):
    if x % 2==0:
        count +=1
    else:
        continue
print(f'0~{num}之间的偶数有{count}个')
'''

'''
for i in range(1,10):
    j = 1
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i}\t',end='')
    print()
'''
# list_base = [21,25,23,22,20]
#
# list_base.append(31)
# list_base.extend([29,33,30])
# ele1 = list_base.pop(0)
# ele2 = list_base.pop(-1)
# query = list_base.index(31)
# print(list_base,ele1,ele2,query)

def test_func(compute):
    result=computer(1,2)
    print(f'输出结果为{result}')

# test_func(lambda x,y:x+y)
def computer(x,y):
    return x+y
test_func(computer)

import my_utils.str_util
from my_utils.file_util import print_file_info

result = my_utils.str_util.str_reverse("大漠孤烟直")
print(result)
print(my_utils.file_util.print_file_info("E:\\text\\bill.txt"))