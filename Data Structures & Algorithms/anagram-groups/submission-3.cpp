class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        std::unordered_map<std::string, vector<std::string>> myMap;

        std::array<int, 26> keyarr;
        std::string key;

        for (int i = 0; i < strs.size(); i++){
            // construct key
            keyarr.fill(0);
            key = "";
            for (char foo : strs[i]){
                keyarr[(foo - 97)]++;
            }
            for (int j = 0; j < keyarr.size(); j++){
                for (int k = 0; k < keyarr[j]; k++){
                    key.push_back(static_cast<char>(j));
                }
            }
            myMap[key].push_back(strs[i]);
        }

        for (auto&[key, value] : myMap){
            result.push_back(value);
        }

        return result;

    }
};
