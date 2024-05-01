# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b = '0'*(len(a)-len(b))+b
        if len(b)>len(a):
            a = '0'*(len(b)-len(a))+a

        ans = ''
        carry = 0
        for i in range(len(a)-1, -1, -1):
            d1, d2 = int(a[i]), int(b[i])
            carry, res = divmod(d1+d2+carry,2)
            ans+=str(res)
        if carry>0:
            ans+=str(carry)
        return ans[::-1]       