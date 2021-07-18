class Solution:
    def tribonacci(self, n: int) -> int:
        n0 = 0
        n1 = 1
        n2 = 1
        tn = 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(3,n+1):
                print(n0,n1,n2)
                tn = n0 + n1 + n2
                n0 = n1
                n1 = n2
                n2 = tn
            return tn
