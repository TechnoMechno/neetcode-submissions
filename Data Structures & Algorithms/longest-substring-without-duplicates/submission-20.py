class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep characters in a hash map for continuous look up
        mySet = set()
        longest = 0
        left = right = 0

        while right < len(s):
            if s[right] not in mySet:
                mySet.add(s[right])
            else:
                while s[right] in mySet:
                    mySet.remove(s[left])
                    left += 1
                mySet.add(s[right])
            
            right += 1
            longest = max(longest, len(mySet))
        
        return longest
