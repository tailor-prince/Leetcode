
#两个数相加
#method 1
nums=[2,7,3,15]
target=18

dict={}
for i in range(len(nums)):
    if (target-nums[i]) not in dict:
        dict[nums[i]]=i
    else:
        print(dict[target-nums[i]],i)

#method 2 暴力法
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            if i>j:
                print(j,i)
            else:
                print(i,j)