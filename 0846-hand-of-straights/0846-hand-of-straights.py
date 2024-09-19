class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time Complexity: O(n * logn)
        # If there is a remainder then we return False 
        if len(hand) % groupSize:
            return False 
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for val in range(first, first + groupSize):
                if val not in count:
                    return False 
                count[val] -= 1
                if count[val] == 0:
                    if val != minH[0]:
                        return False 
                    heapq.heappop(minH)
        return True 