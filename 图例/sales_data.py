# 定义抽象类，定义文件读取功能
from datadefine import dataDefine
import json

class readFile:

    def read_data(self):
        pass

class textFileReader(readFile):

    def __init__(self,road):
        self.road = road   # 定义成员变量：记录文件路径

    # 复写抽象方法
    def read_data(self):
        f = open(self.road,'r',encoding='utf-8')
        record_list = []
        for line in f.readlines():
            line =line.replace('\n','')
            # print(line)
            data_list = line.split(',')
            # 将data_list中的元素传递给dataDefine
            record = dataDefine(data_list[0],data_list[1],float(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class jsonFileReader(readFile):

    def __init__(self,road):
        self.road = road   # 定义成员变量：记录文件路径

    def read_data(self):
        f = open(self.road, 'r', encoding='utf-8')
        record_list = []
        for line in f.readlines():
            data_line = json.loads(line)
            record = dataDefine(data_line["date"],data_line["order_id"],data_line["money"],data_line["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file = textFileReader(r'E:\选题\2011年1月销售数据.txt')
    json_file = jsonFileReader(r'E:\选题\2011年2月销售数据JSON.txt')
    tl = text_file.read_data()
    jl = json_file.read_data()

    for i in tl:
        print(i)

    for j in jl:
        print(j)