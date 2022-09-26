def print_file_info(file_name):
    f1 = None
    try:
        f1 = open(file_name,'r',encoding="utf-8")
        print(f'{file_name}的内容为：{f1.readlines()}')
    except Exception as e:
        print(f'文件路径不存在,原因是{e}')
    finally:
        if f1:     # 如果文件路径不存在，f1是false对象
            f1.close()

def append_to_file(file_name,data):
    f2 = None
    try:
        f2 = open(file_name,'w',encoding="utf-8")
        f2.write(data)
        f2.write('\n')
    finally:
        f2.close()


if __name__ == '__main__':
   print_file_info('E:\\text\\bak.txt')