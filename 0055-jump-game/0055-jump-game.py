class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # we will work our way backwards 
        goal = len(nums) - 1
   
        # we travel backwards 
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i 
        
        return True if goal == 0 else False 
 
