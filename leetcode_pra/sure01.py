# print(chr(98))
# print(ord('谢'))
# fp=open('text.txt','w')
# print('人生苦短，我用Python',file=fp)
# fp.close()
# import os
# os.remove(r'.\\text.txt')

# print(bool(-1))
# print(10/0 or 8>7)


# farther_height=eval(input('请输入父亲的身高：'))
# mother_height=eval(input('请输入母亲的身高：'))
# son_height=0.54*(farther_height+mother_height)
# print('儿子预期身高：',round(son_height,1))

# lst=['hello','world','python']
# lst.pop(1)
# print(lst)
'''
import random

lst1 = [i for i in range(1, 100) if i % 3 == 0]
lst2 = [random.randint(1,100) for i in range(10)]
lst3 = [1 for _ in range(10)]
print(lst1,lst2,lst3,sep='&')
'''

dict1 = {'hello':1,'world':2,'python':3}
print(dict1['hello'])
print(dict1.get('java','无结果'))
# dict1.pop('hello')
# dict1.pop(1)
print(dict1)

lst1 = [1001,1002,1003]
lst2 = ['chen meimei','li lily','wang yiyi']
dict2 = {key:value for key,value in zip(lst2,lst1)}
print(dict2)


