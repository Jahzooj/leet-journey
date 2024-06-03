class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        i2l = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        if digits == "":
            return []
        if len(digits) == 1:
            return i2l[digits[0]]

        letters = []
        for i in digits:
            letters.append(i2l[i])

        q = [(x ,0) for x in i2l[digits[0]]]
        ans = []
        while q:
            curr = q.pop(0)
            last_letter = curr[0][-1]
            index = curr[1] + 1
            if index < len(letters):
                nbors = letters[index]
                for n in nbors:
                    q.append((curr[0] + n,curr[1] + 1))
            else:
                ans.append(curr[0])

        return ans
