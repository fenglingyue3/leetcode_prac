'''
[88,89,98,99,0,90]
↓
[1998,1989,1999,2000,1990]
'''

lst = [88,89,98,99,00,90]
# print(lst)
'''
# 遍历列表
for index in range(len(lst)):
    if  str(lst[index]) != '0':
        lst[index] = '19'+ str(lst[index])
    else:
        lst[index] = '200'+ str(lst[index])

# 修改后的列表
print(lst)
'''
# 使用enumerate函数
for index,value in enumerate(lst):
    if str(lst[index]) !='0':
        lst[index] = '19' + str(value)
    else:
        lst[index] = '200' + str(value)

print(lst)