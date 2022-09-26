import  json

# 从文件中读取数据
f_us = open(r'E:\选题\资料\可视化案例数据\折线图数据\美国.txt','r',encoding='utf-8')
content = f_us.read()
# 规整数据
content =content.replace('jsonp_1629344292311_69436(','')
content =content[:-2]
us_dict = json.loads(content) # 将json数据转换成字典
# print(type(us_dict))
trend = us_dict['data'][0]['trend']
# print(trend)

# 获取x轴数据
us_x = trend['updateDate'][:314]

# 获取y轴数据
us_y = trend['list'][0]['data'][:314]

# 生成折线图


# 关闭文件对象
f_us.close()