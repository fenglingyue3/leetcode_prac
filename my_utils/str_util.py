def str_reverse(s):
    return s[::-1]

def subStr(s,x,y):
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("白日依山尽"))
    print(subStr("白日依山尽",1,3))