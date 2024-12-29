class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters_s = {}
        characters_t = {}

        for c in s:
            if c not in characters_s:
                characters_s[c] = 1
            else:
                characters_s[c] += 1
        
        for c in t:
            if c not in characters_t:
                characters_t[c] = 1 
            else:
                characters_t[c] += 1
        
        return characters_s == characters_t
