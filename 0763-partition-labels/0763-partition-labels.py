class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Time Complexity: O(n)
        lastIndex = {} #char -> last index in s 

        for i,c in enumerate(s):
            lastIndex[c] = i 

        res = []
        size, end = 0, 0 
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                # reset the size to 0 
                size = 0 
        return res 
