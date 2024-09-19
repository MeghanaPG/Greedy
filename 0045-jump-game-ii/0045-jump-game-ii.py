class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 

        l = r = 0 

        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            # right next to the window we are considering 
            l = r + 1 
            r = farthest
            # Indicates the number of jumps 
            res += 1
        return res