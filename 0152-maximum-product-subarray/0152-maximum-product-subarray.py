class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1 

        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue 
            
            temp = curMax * n 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, temp, n)
            res = max(res, curMax)
        return res