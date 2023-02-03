#include <string>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b) {
    return(a[0] < b[0]);
}

int solution(vector<vector<string>> book_time) {
    int answer = 0;
    
    vector<vector<int>> timeArr;
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int i = 0; i < book_time.size(); i++) {
        string startTime = book_time[i][0];
        string endTime = book_time[i][1];
        
        int s_hour = stoi(startTime.substr(0, 2)) * 60;
        int s_minute = stoi(startTime.substr(3, 2));
        int e_hour = stoi(endTime.substr(0, 2)) * 60;
        int e_minute = stoi(endTime.substr(3, 2)) + 10;
        
        timeArr.push_back({s_hour + s_minute, e_hour + e_minute});
    }
    
    sort(timeArr.begin(), timeArr.end(), cmp);
    
    for (int i = 0; i < timeArr.size(); i++) {
        
        int tmp = timeArr[i][0];
        
        if (pq.size() == 0) {
            pq.push(timeArr[i][1]);
        }
        
        else if (pq.size() != 0 && tmp >= pq.top()) {
            pq.push(timeArr[i][1]);
            pq.pop();
        }
        
        else {
            pq.push(timeArr[i][1]);
        }
    }
    
    answer = pq.size();
    
    return answer;
}