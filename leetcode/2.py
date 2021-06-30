class Solution:
    def interpret(self, n):
        return n.replace('()', 'o').replace('(al)', 'al')