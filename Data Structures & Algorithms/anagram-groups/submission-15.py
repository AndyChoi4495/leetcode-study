class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            group = [0] * 26
            for c in s:
                group[ord(c) - ord('a')] += 1
            res[tuple(group)].append(s)

        
        return list(res.values())
    



        