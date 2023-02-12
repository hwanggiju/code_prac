#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index) {
    
    string answer = "";
    
    for (auto i : s)
    {
        int cnt = 0;
        int atoz = i - 'a';
        
        while(cnt < index)
        {
            atoz++;
            i = (atoz % 26) + 'a';
            if(skip.find(i) == string::npos)
            {
                cnt++;
            }
        }
        answer += i;
    }
    return answer;
}