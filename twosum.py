class Solution:
    def __init__(self):
        pass
    def twoSum(self, nums, target):
        num=list(nums)
        l=len(num)
        result=[]
        for i in range(l):
            for j in range(1,l,1):
                x=num[i]+num[j]
                if x==target and i!=j:
                    result.append(i)
                    result.append(j)
                    b=set(result)
                    c=list(b)
        return c
a= Solution()
print(a.twoSum([-1,-2,-3,-4,-5],-8))