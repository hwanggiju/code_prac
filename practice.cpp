#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    int answer = 0;
    int sum = 0;
    priority_queue<int, vector<int>> pq;
    
    for (int i = 0; i < enemy.size(); i++) {
        
        sum += enemy[i];
        
        if (sum <= n) {
            pq.push(enemy[i]);
            answer += 1;
        }
        
        else if (k > 0) {
            k -= 1;
            pq.push(enemy[i]);
            int tmp = pq.top();
            pq.pop();
            sum -= tmp;
            answer += 1;
        }
            
        else break;
    }
    
    return answer;
}