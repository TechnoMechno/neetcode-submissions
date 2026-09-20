class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;

        while (start < end){
            while (!std::isalnum(s[start])){
                start++;
            }
            while (!std::isalnum(s[end])){
                end--;
            }
            if (start < end){
                char charStart = std::tolower(s[start]);
                char charEnd = std::tolower(s[end]);

                if(charStart != charEnd) return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
