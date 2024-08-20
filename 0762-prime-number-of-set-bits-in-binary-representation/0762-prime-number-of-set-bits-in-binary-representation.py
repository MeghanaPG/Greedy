class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Time Complexity: O(n)
        def isPrime(n):
            count = 0 
            for i in range(1,n+1):
                if n % i == 0:
                    count += 1
            if count == 2:
                return True #prime divisible by 1 and itself
            else:
                return False 
        countp = 0
        for i in range(left,right+1):
            ans = bin(i).count("1")
            if isPrime(ans):
                countp += 1
        return countp