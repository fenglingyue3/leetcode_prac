str1 = 'itheima'
str2 = 'collcene'

def my_len(data):
    count = 0
    for i in  data:
        count += 1
    print(f'字符串{data}的长度为{count}')

my_len(str1)
my_len(str2)

temperature = float(input('测量体温：'))
def wel():
    if temperature <=37.5:
        print(f'欢迎！\n您的体温{temperature}℃正常，请进。')
    else:
        print(f'欢迎！\n您的体温{temperature}℃,需要隔离。')

wel()

