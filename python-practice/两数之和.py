# def twoSum(nums,target):
#     lens = len(nums)
#     j = -1
#     for i in range(1,lens):
#         temp = nums[:i]
#         if (target - nums[i]) in temp:
#             j = temp.index(target - nums[i])
#             break
#     if j>=0:
#         return[j,i]
# 
# res1 = twoSum([1,2,5,10,3,8,7],10)
# print(res1)

def twoSum(nums,target):
    for i in range(len(nums)):
        res = target - nums[i]
        if res in nums[i+1:]:
            j = nums[i+1:].index(res)+i+1
            return[i,j]

res1 = twoSum([1,2,5,10,3,8,7],10)
print(res1)

        
