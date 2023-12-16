class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        maxSub = nums[0]
        curSum = 0 

        for n in nums:
            if curSum < 0:
                curSum = 0 
            curSum += n 
            maxSub = max(maxSub, curSum)
        return maxSub 
        