# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n:
            if n&1:
                bit_count+=1
            n=n>>1
        return bit_count
        