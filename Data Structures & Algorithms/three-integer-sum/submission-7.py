class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tmp = None
        triplets = []
        tmp = None
        print(nums)
        for i in range(len(nums)):
            if nums[i] == tmp:
                continue
            triplet = self.findPair(nums, -nums[i], i+1)
            for x in triplet:
                if x:
                    triplets.append(x)
            tmp = nums[i]
        return triplets


    def findPair(self, nums:List[int], target: int, start: int) -> List[List[int]]:
        d = {}
        pairs = []
        for i in range(start,len(nums)):
            diff = target - nums[i]
            if diff in d:
                if d[diff] == None:
                    pairs.append([-target, nums[i], diff])
                    d[diff] = nums[i] 
            else:
                d[nums[i]] = None
        return pairs
                

