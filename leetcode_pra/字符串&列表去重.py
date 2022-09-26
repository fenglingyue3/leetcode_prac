s = 'HelloWorld'
new_str1 = ''
#使用字符元素遍历拼接
for item in s:
    if item not in new_str1:
        new_str1+=item
print(new_str1)

#使用索引遍历

new_str2 = ''
for index in  range(len(s)):
    if s[index] not in new_str2:
        new_str2 +=s[index]
print(new_str2)

#使用集合+列表排序
new_str3 = set(s)
# print(new_str3)
l=list(new_str3)
l.sort(key=s.index) #排序关键字
print(''.join(l))

lst1 = ['金星','木星','水星','火星','土星','金星','木星','水星','火星','土星']

#使用元素遍历
new_lst1=[]
for i in lst1:
    if i not in new_lst1 :
        new_lst1.append(i)
print(new_lst1)

#使用索引遍历
new_lst2=[]
for index in  range(len(lst1)):
    if lst1[index] not in new_lst2:
        new_lst2.append(lst1[index])
print(new_lst2)

#使用set+排序
s_lst=set(lst1)
new_lst3=list(s_lst)
new_lst3.sort(key=lst1.index)
print(new_lst3)
