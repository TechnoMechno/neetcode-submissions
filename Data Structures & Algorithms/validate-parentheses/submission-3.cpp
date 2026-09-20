class Solution {
public:
    bool isValid(string s) {
        // check if round, square, curly
        // check if open or close

        // if open -> push to stack
        // if closed -> check top

        std::stack<char> myStack;
        for (char letter : s){
            if (letter == '(' || letter == '{' || letter == '[')
                myStack.push(letter);
            else if (letter == ')' || letter == '}' || letter == ']'){
                char top = myStack.top();
                if (myStack.empty())
                    myStack.push(letter);
                else if (top == '(' && letter == ')')
                    myStack.pop();
                else if (top == '[' && letter == ']')
                    myStack.pop();
                else if (top == '{' && letter == '}')
                    myStack.pop();
                else
                    myStack.push(letter);
            }
        }
        if (myStack.empty()){
            return true;
        }
        return false;
    }
};
