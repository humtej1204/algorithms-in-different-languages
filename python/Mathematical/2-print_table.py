#!/usr/bin/env python3

"""
function getTable() which takes an integer N as input parameter
and returns a list of integers denoting the multiplication of
table of N from 1 to 10
"""
class Solution:
    def getTable(self,N):
        ls = []
        for x in range(1, 10 + 1):
            ls.append(N * x)
        return ls

#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
