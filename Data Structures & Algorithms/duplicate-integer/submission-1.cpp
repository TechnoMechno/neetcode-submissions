class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> myMap;

        for (int x : nums){
            // if number is present
            if (myMap.count(x)) return true;
            myMap.insert(x);
        }

        return false;
    }
};