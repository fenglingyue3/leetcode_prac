from datadefine import dataDefine
from sales_data import readFile,jsonFileReader,textFileReader

text_file = textFileReader(r'E:\选题\2011年1月销售数据.txt')
json_file = jsonFileReader(r'E:\选题\2011年2月销售数据JSON.txt')

jan_data = text_file.read_data()
fab_data = json_file.read_data()
all_data = jan_data + fab_data

data_dict = {}
for record in  all_data:
    try:
        data_dict[record.date] += record.money
    except:
        data_dict[record.date] = record.money

print(data_dict)

