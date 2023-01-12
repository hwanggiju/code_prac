#include <string>
#include <vector>
#include <stack>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups)
{
    long answer = 0;
    
    int idx = n - 1;
    
    int d_box = 0;
    int p_box = 0;
    
    while (idx >= 0) {
        
        d_box += deliveries[idx];
        p_box += pickups[idx];
        
        while (d_box > 0 || p_box > 0) {
            d_box -= cap;
            p_box -= cap;
            answer += (idx + 1) * 2;
        }
        
        idx--;
        
    }
    
    return answer;
}