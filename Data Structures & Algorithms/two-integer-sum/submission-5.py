class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in map:
                return [map[tmp],i]
            map[nums[i]] = i
        return []
        