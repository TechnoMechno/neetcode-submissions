class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep characters in a hash map for continuous look up
        mySet = set()

        counter = 0
        max = 0
        i = 0
        j = 0
        while (i < len(s)):
            # print(s[i],counter)
            if s[i] not in mySet:
                mySet.add(s[i])
                counter += 1
            else:
                if counter > max:
                    max = counter
                # remove elements from the left until theres no more        duplicate
                while s[i] in mySet:
                    mySet.remove(s[j])
                    j += 1
                    counter -= 1
                mySet.add(s[i])
                counter +=1
            
            i += 1

                
                
        
        if max < counter:
            max = counter

        return max


        