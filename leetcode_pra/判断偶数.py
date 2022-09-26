'''
def even_num(lise_user):
    list_base= []
    i = 0
    while  i < len(lise_user):
        ele = lise_user[i] % 2
        if ele == 0:
            list_base.append(lise_user[i])
        else:
            pass
        i += 1
    # for i in lise_user:
    #     if i % 2 == 0:
    #         list_base.append(i)
    print(list_base)

even_num([1,2,3,4,5,6,7,8,9,10])
'''
'''
tup1=('周杰伦',11,['football','music'])
age = tup1.index(11)
name = tup1[0]
# print(f'学生姓名：{name}，年龄：{age}')
tup1[2].remove('football')
hobby_add = tup1[2].append('coding')
print(tup1)
'''

'''
str_base = "itheima itcast boxuegu"
num_it = str_base.count('it')
print(f'字符串{str_base}中it的数量为{num_it}个')
newStr1 = str_base.replace(" ","|")
print(f'字符串{str_base}，被替换空格后，表现为{newStr1}')
newStr2 = newStr1.split("|")
print(f'字符串{newStr1}，按照|分割后得到{newStr2}')
'''
str_base = "万过新月，员序程马黑，nohthp学"
'''
str1 = str_base[::-1]
# print(f'{str_new[8:13]}')
str2 = str1.strip("学python，")
str3 = str2.strip("，月新过万")
print(str3)
'''
# str_new = str_base.replace("万过新月，员序程马黑，nohthp学","黑马程序员")
# print(str_new)

my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
# my_set = set(my_list)
my_set = set()
for i in  my_list:
    my_set.add(i)
print(f'{my_set}')