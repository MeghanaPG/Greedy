class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time Complexity: O(n)
        # leftMin: minimum possible number of unmatched left parentheses
        # leftMax: maximum possible number of unmatched left parentheses
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1 
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                # this is in case of the wildcard 
                leftMin, leftMax = leftMin - 1 , leftMax + 1 
            if leftMax < 0:
                return False 
            if leftMin < 0: # s = ( * ) (
                leftMin = 0 
        return leftMin == 0 
