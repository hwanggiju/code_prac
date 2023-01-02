#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int col_tmp;

bool cmp (vector<int>& x, vector<int>& y) {
    if (x[col_tmp - 1] < y[col_tmp - 1])
        return true;
    
    if (x[col_tmp - 1] > y[col_tmp - 1])
        return false;
    
    if (x[col_tmp - 1] == y[col_tmp - 1]) {
        if (x[0] > y[0])
            return true;
        else
            return false;
    }
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    int answer = 0;
    int tmp = 0;
    col_tmp = col;
    
    sort(data.begin(), data.end(), cmp);
    
    for (int i = row_begin - 1; i < row_end; i++) {
        int sum = 0;
        
        for (int j = 0; j < data[i].size(); j++) {
            sum += (data[i][j] % row_begin);
        }
        if (tmp == 0)
            tmp = sum;
        else tmp = tmp ^ sum;
        
        row_begin += 1;
    }
    
    answer = tmp;
    
    return answer;
}