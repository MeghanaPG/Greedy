class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        sorted_str_list = []

        anagram_hash_table = {}

        for each in strs:
            sorted_str = "".join(sorted(each))
            sorted_str_list.append(sorted_str)

        for i, key in enumerate(sorted_str_list):
            if key in anagram_hash_table:
                anagram_hash_table[key].append(strs[i])
            else:
                anagram_hash_table[key] = [strs[i]]
        
        return list(anagram_hash_table.values())