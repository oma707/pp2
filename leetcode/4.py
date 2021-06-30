class Solution:
    def largestAltitude(self, n):
        res = 0
        start = 0
        for i in n:
            start += i
            res = max(res, start)

        return res