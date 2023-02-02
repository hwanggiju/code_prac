#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> numbers) {
    int n = numbers.size();
    
    vector<int> answer(n, -1);
    stack<int> s;
    
    for (int i = 0; i < n; i++) {

        int tmp = numbers[i];
        
        while (!s.empty()) {
            if (numbers[s.top()] < tmp) {
                answer[s.top()] = tmp;
                s.pop();
            }
            else {
                break;
            }
        }
        
        s.push(i);
    }
    return answer;
}