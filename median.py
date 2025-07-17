class Solution():
    def __init__(self):
        pass
    def findMedianSortedArrays(self):
        l1=[1,2]
        l2=[3,4]
        sum=0
        addd=l1+l2
        for i in range (len(addd)):
            for j in range(i+1,len(addd),1):
                if addd[i]>addd[j]:
                    dummy=addd[i]
                    addd[i]=addd[j]
                    addd[j]=dummy
        print(addd)            
        l=len(addd)
        if l%2==1:
            pos=int((l/2)-(1/2))
            median=addd[pos]
        else:
            pos1=int(l/2)
            pos2=int(pos1-1)
            median=(addd[pos1]+addd[pos2])/2
        return median
a=Solution()
print(a.findMedianSortedArrays())