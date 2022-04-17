#!/usr/bin/env python3
"""
the function nthTermOfAP() which takes three integers A1,A2 and N as
input parameters and returns the nth term of the AP that has A1 and A2
as the first and second terms respectively.
"""
class Solution:
    def nthTermOfAP(self,A1,A2,N):
        k = A2 - A1
        r = A1 + (k * (N-1))
        return r

#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A1,A2,N=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.nthTermOfAP(A1,A2,N))
