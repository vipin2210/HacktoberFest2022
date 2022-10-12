//LeetCode popular Question for beginner
// 412. Fizz Buzz

//Question is as follow:
// Given an integer n, return a string array answer (1-indexed) where:
// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.
//We just have to complete the Function :)

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> arr;
        for(int i=1; i<=n ;i++){
            if(i%3==0 && i%5==0)
                arr.push_back("FizzBuzz");
            else if(i%3==0)
                arr.push_back("Fizz");
            else if(i%5==0)
                arr.push_back("Buzz");
            else
                arr.push_back(to_string(i));
        }
        return arr;
    }
};

// Runtime: 3 ms
// Memory Usage: 8 MB