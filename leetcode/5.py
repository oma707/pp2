class Solution(object):
    def ProdAndSum(self, n):


        st = str(n)
        productNum = 1
        sumNum = 0

        for i in st:
            productNum *= int(i)
            sumNum += int(i)

        return productNum - sumNum