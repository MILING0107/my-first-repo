def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]
    
res1 = twoSum([1,2,5,10,3,8,7],10)
print(res1)

res2 = twoSum([3,3],6)
print(res2)

res3 = twoSum([2,7,11,15],9)
print(res3)
     
            
             
     