'''
str1 = 'Hello'
str2 = 'World'
print(str1+str2) #1）使用+拼接字符串

print(' % '.join(['python','java','php','go'])) #2）使用join拼接字符串

print('hello''world') #3）直接拼接

print('%s%s' % (str1,str2)) #格式化字符串拼接
print(f'{str1}{str2}')
print('{}{}'.format(str1,str2))
'''

import re

s1 = '3.10python I study everyday'
pattern = r'\d\.\d+'
match2 = re.match(pattern,s1,re.I)
print('起始位置：',match2.start())
print('终止位置：',match2.end())
print('区间：',match2.span())
print('匹配的字符：',match2.string)
print('匹配结果：',match2.group())

pattern = '黑客|破解|反爬'
s1 = '我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s = re.sub(pattern,'**',s1)
print(new_s)

s2 = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%98%8E%E6%98%9F%E5%A4%A7%E4%BE%A6%E6%8E%A2%E7%AC%AC%E4%B8%83%E5%AD%A3&fenlei=256&rsv_pq=9b6e809f00008ca5&rsv_t=dfacBzBlI9BrrAss5x1VctGmNzl4VZj0f4CYD0vD5%2FiJwwaWLYLBdQBynAw&rqlang=cn&rsv_enter=1&rsv_dl=ih_1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsv_btype=i&rsp=1&rsv_sug9=es_2_1&rsv_sug4=1397&rsv_sug=9'
pattern = '[?|&]'
new_lst = re.split(pattern,s2)
print(new_lst)