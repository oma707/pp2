class Solution:
    def numIdenticalPairs(self, a):
        c=0
        i=0
        j=i+1
        n=len(a)
        while i<j and j<n+1:
            if j==n:
                i=i+1
                j=i+1
            if i==n-1:
                break
            if a[i]==a[j]:
                c=c+1
                j=j+1
            else:
                j=j+1
        return c