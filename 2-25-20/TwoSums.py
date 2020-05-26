class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index, index2 in enumerate(nums):
            answer = target - index2
            if answer in d:
                return [d[answer], index]
            d[index2] = index
        return []