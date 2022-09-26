'''
d = {'a':10,'b':20,'c':30,'d':40}
d2 = d
d['b'] = 100
print(d['b']+d2['b'])

lst =[]
for i in '想念':
    for j in '家人':
        lst.append(i+j)
print(lst)
'''


str1 = 'HelloWorld'
str2 = str1.lower()
str3 = str1.upper()
print(str2,'  ',str3)
print(str1.center(20,'*'))  # 居中对齐
print('   hello  world  '.strip()) # 去除空格
print('dl-hello world'.strip('dl')) #去除制定字符
print('{0:*>20}'.format(str1)) #使用format对齐字符
print('{0:*^20}'.format(str1))

name = '韩梅梅'
age = 18
score = 98.5
print('姓名：%s,年龄：%d,成绩:%.2f' % (name,age,score)) #占位符格式化字符
print(f'姓名：{name},年龄：{age},成绩：{score}') # f-string格式化字符
print('姓名：{},年龄：{},成绩：{}'.format(name,age,score)) # format格式化字符串
print('姓名：{2},年龄：{0},成绩：{1}'.format(age,score,name))

print('{0:.5f}'.format(3.1415926))
print('{0:.5}'.format('helloworld'))
