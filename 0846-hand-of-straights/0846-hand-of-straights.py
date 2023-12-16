class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time Complexity: O(n*logn)
        if len(hand) % groupSize:
            return False 
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        # we want minHeap with distinct values that are available to us 
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False 
                count[i] -= 1 
                if count[i] == 0:
                    # if the value we are popping is not the min val then we will return false immediately 
                    if i != minH[0]:
                        return False 
                    heapq.heappop(minH)
        return True 


