class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        ans = []

        for s in strs:
            ss = ''.join(sorted(s))

            if ss in sets:
                sets[ss].append(s)
            else:
                sets[ss] = [s]

        for s in sets:
            ans.append(sets[s])

        return ans
            