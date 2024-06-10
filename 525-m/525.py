class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {}

        best = 0
        new_val = 0
        for i, n in enumerate(nums):
            step = 1 if n == 1 else -1
            new_val += step

            if new_val == 0:
                best = i + 1
            elif new_val in sums:
                subarr = i - sums[new_val]
                best = subarr if subarr > best else best
                continue
            else:
                sums[new_val] = i

            


        return best
