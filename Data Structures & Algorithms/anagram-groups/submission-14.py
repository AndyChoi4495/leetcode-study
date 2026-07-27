class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # using asci code
        res = defaultdict(list)

        for s in strs:
            cnt = 26 * [0]
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            res[tuple(cnt)].append(s)
        
        return list(res.values())
