staff = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2
    }
}
'''
print(staff)
person = staff.keys()
# print(person)
for k in person:
    if staff[k]["级别"] == 1:
        staff[k]["级别"] += 1
        staff[k]["工资"] += 1000
'''
for name in staff: # for循环遍历字典
    if staff[name]["级别"] == 1:
        # 获取员工信息字典
        staff_info = staff[name]
        # print(staff_info)
        staff_info["级别"] += 1
        staff_info["工资"] += 1000
        # 将员工信息更新回字典
        staff[name] = staff_info


print(staff,type(staff))
