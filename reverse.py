class Solution():
    def __init__(self):
        pass
    def reverse(self, x):
        rev=0
        remainder=0
        if x >=0:
            for i in range(len(str(x))):
                remainder=x%10
                rev=rev*10+remainder
                x=int(x/10)
        else:
            x=x*-1
            for i in range(len(str(x))):
                remainder=x%10
                rev=rev*10+remainder
                x=int(x/10)
            rev=rev*-1
        if  (rev> 2147483647) or  (rev< -2147483648):
            return 0
        else:
            return rev  
c=Solution()
print(c.reverse(321))