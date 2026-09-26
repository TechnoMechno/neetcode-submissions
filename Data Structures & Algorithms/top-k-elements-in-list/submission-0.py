class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hash map to count numbers (number : frequency)
        myDict = {}
        # build list of list to insert numbers based on their frequency. (frequency = index)
        myList = [[] for _ in range(len(nums) + 1)]

        ret = []
        # Build hash map
        for x in nums:
            myDict[x] = myDict.get(x,0) + 1
        # insert numbers into list
        for key, value in myDict.items():
            myList[value].append(key)
        
        # interate list from right to left
        for subList in reversed(myList):
            for x in subList:
                ret.append(x)
                k = k - 1
                if k == 0:
                    break
            
            if k == 0:
                break
        
        return ret