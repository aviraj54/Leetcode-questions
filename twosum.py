class Solution:
    def __init__(self):
        pass
    def twoSum(self, nums, target):
        num=list(nums)
        l=len(num)
        result=[]
        for i in range(l):
            R=target-num[i]
            if R in num and (num[i]!=R or num[i+1]==R):
                    result.append(i)
        return result
a= Solution()
print(a.twoSum([3,3],6))