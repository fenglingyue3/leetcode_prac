import re

'''
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)',double,s))
'''

str_before = re.split('\W+', ' runoob1, runoob02, runoob.', 1)
# print(str_before)
# for i in range(len((str_before))):
    # print(type(str_before))
    # temp = ''
    # if len(str_before[i-1]) < len(str_before[i]):
    #     temp = str_before[i]
    #     print(type(str_before[i]))
    # elif len(str_before[i-1]) >= len(str_before[i]):
    #     temp = str_before[i-1]
    # else:
    #     print('error!')
'''
n = len(str_before)

for i in range(n):
    for j in range(n-i-1):
        if len(str_before[j])>len(str_before[j+1]):
            str_before[j],str_before[j+1] = str_before[j+1],str_before[j]
print(str_before[j+1])
'''
str_list = []
for i in range(len(str_before)):
    # str_list = list(len(str_before))
    #
    str_list.append(len(str_before[i]))
    print(str_list)
