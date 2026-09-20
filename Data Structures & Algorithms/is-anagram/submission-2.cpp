class Solution {
public:
    bool isAnagram(string s, string t) {
        // check length
        if (s.size() != t.size()) return false;
        
        std::unordered_map<int, int> myMap;

        for (int s_i = 0, s_t = 0; s_i < s.size(); ++s_i, ++s_t){
            myMap[s[s_i]]++;
            myMap[t[s_t]]--;
        }

        for (auto& pair: myMap){
            if (pair.second != 0){
                return false;
            }
        }

        return true;
    }
};
