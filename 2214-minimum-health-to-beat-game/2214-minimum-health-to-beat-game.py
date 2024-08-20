class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # Time and Space: O(1)
        maxDamage = 0
        totalDamage = 0 

        for d in damage:
            totalDamage += d 
            maxDamage = max(maxDamage, d)
        
        return totalDamage - min(armor, maxDamage) + 1
       