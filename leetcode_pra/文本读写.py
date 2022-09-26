'''
f = open(r'E:\text\test_text.txt','r',encoding='utf-8')

#一次性取出
num = f.read().count('itheima')
print(num)
#遍历文件
f.close()
'''

with open('E:\\text\\bill.txt','r',encoding="utf-8") as f1:
    '''
    for line in f1:
        f2 = open('E:\\text\\bak.txt','w',encoding="utf-8")
        if line != "测试":
            f2.write(line)
        else:
            continue
        f2.close()
'''
    f2 = open('E:\\text\\bak.txt','w',encoding="utf-8")
    for line in f1:
        line = line.strip() # 去除每段/n
        # 判断条件写入文件
        if line.split(",")[4] == "测试":
            continue
        else:
            f2.write(line)
            f2.write("\n")
    f2.close()
