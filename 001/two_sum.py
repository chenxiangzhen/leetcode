class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return d

s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
print(result)