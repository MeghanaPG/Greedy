from collections import Counter
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        cnt = collections.Counter(s)
        added = []
        for idx, c in enumerate(s):
            if c == "?":
                min_char, choose_c = float("inf"), ""
                for i in range(26):
                    cur_c = chr(i + ord("a"))
                    if cnt[cur_c] < min_char:
                        min_char, choose_c = cnt[cur_c], cur_c
                cnt[choose_c] += 1
                added.append(choose_c)
        
        added.sort()
        j = 0
        res = []
        for c in s:
            if c != "?":
                res.append(c)
            else:
                res.append(added[j])
                j += 1 
        return "".join(res)