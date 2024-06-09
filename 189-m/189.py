class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        visited = 0
        original_index = 0
        while visited < len(nums):
            index = original_index
            prev = None
            while True:
                if prev is None:
                    prev = nums[index]
                    index = (index + k) % len(nums)
                    visited += 1
                    continue

                # swap
                t = nums[index]
                nums[index] = prev
                prev = t

                index = (index + k) % len(nums)
                visited += 1

                if index == original_index and prev is not None:
                    nums[original_index] = prev
                    original_index += 1
                    break

