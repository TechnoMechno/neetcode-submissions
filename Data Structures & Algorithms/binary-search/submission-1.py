class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        return self.binSearch(nums, left, right, target)


    
    def binSearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        mid = (right + left) // 2
        if left > right:
            return -1
        elif nums[mid] == target:
            return mid
        
        # if target > mid, search right
        elif target > nums[mid]:
            return self.binSearch(nums, mid+1, right, target)
        # if target < mid, search left
        else:
            return self.binSearch(nums, left, mid-1, target)
        