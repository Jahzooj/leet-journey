class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsf = nums[0]
        minsf = nums[0]
        maxans = max(nums)

        for n in nums[1:]:
            if n == 0:
                maxsf, minsf = 1, 1
                continue

            t = n * maxsf
            maxsf = max(t, n * minsf, n)
            minsf = min(t, n * minsf, n)

            maxans = max(maxsf, minsf, maxans)

        return maxans