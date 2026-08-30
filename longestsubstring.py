class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=0
        valid=False
        pos=0
        d={}
        f=[]
        for i in range(len(s)):
            l=[]
            for j in range(i+1,len(s)+1):
                s1=s[i:j]
                l.append(s1)
            f.append(l)
        for k in range(len(f)):
            for x in (f[k]):
                if len(x)==len(set(x)):
                    if len(x)>pos:
                        pos=len(x)
        return pos