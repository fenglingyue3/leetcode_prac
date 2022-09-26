'''
import  time

def twoSum(nums,target):
    # t1 = time.time()
    j=-1
    lens=len(nums)
    for i in  range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target-nums[i])==1)&(target-nums[i]==nums[i]):
                continue
            else:
                j = nums.index(target - nums[i],i+1)
                break
    # t2 = time.time()
    # ts = t2 - t1
    # print(ts)

    if j > 0:
        return  [i,j]

    else:
        return []


print(twoSum([2,7,11,15,3,4,5,6,10,12,13],9))

# 真·两数之和
print('输入的两数之和为：%.2f' % (float(input('请输入第一个数：'))+float(input('请输入第一个数：'))))
'''

num1 = float(input('输入第一个数字：'))
num2 = float(input('输入第二个数字：'))

print(f'{num1}、{num2}两数之和为:%.2f'%(num1+num2))