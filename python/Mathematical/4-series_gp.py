# Optimized way to do whis task
class Solution:
    def powm(self, x, n, M):
        result = 1
        
        while (n > 0):
            """ If n is not a pair number """
            if (n % 2 == 1):
                result = (result * x) % M

            x = (x * x) % M

            """ Casting n to not get float numbers """
            n = int(n / 2)
        return result
        
    def Nth_term(self, a, r, n):
        mod = 1000000007
        res = self.powm(r, n - 1, mod)
        res = res * a
        res = res % mod
        return res

# Main function
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        a, r, n = input().split()
        a = int(a)
        r = int(r)
        n = int(n)
        ob = Solution()
        ans = ob.Nth_term(a, r, n)
        print(ans)
