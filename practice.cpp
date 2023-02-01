#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int x, int y, int n) {
    int answer = 1;
    vector<int> nodeLst;
    
    if (x == y) {
        return 0;
    }
    
    int a = x + n;
    int b = x * 2;
    int c = x * 3;
    
    if (a < y) {
        nodeLst.push_back(a);
    }
    else if (a == y) {
        return answer;
    }
    
    if (b < y) {
        nodeLst.push_back(b);
    }
    else if (b == y) {
        return answer;
    }
    
    if (c < y) {
        nodeLst.push_back(c);
    }
    else if (c == y) {
        return answer;
    }
    
    while (true) {
        answer += 1;
        vector<int> newnodeLst;
        
        for(int i = 0; i < nodeLst.size(); i++) {
            int _plus = nodeLst[i] + n;
            int _dou = nodeLst[i] * 2;
            int _tri = nodeLst[i] * 3;
            
            if (_plus < y) {
                newnodeLst.push_back(_plus);
            }
            else if (_plus == y) {
                return answer;
            }
            
            if (_dou < y) {
                newnodeLst.push_back(_dou);
            }
            else if (_dou == y) {
                return answer;
            }
            
            if (_tri < y) {
                newnodeLst.push_back(_tri);
            }
            else if (_tri == y) {
                return answer;
            }
        }
        
        if (newnodeLst.size() == 0) {
            return -1;
        }
        
        sort(newnodeLst.begin(), newnodeLst.end());
        newnodeLst.erase(unique(newnodeLst.begin(), newnodeLst.end()), newnodeLst.end());
        nodeLst = newnodeLst;
        
    }
    
    
    return answer;
}