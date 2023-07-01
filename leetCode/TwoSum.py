import os 


def twoSum(nums, target):
    ans = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                ans.append(i)
                ans.append(j)
    print(ans)
    return ans

twoSum(nums=[4, 5, 1, 9], target=5)