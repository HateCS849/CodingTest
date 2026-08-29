#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    int n = elements.size();
    
    vector<long long> doubleElements(2 * n, 0);
    for (int i = 0; i < 2 * n; i++){
        doubleElements[i] = elements[i % n];
    }
    set<long long> sums;
    for(int i = 0; i < n; i++){ //시작점
        long long sum = 0;
        for(int len = 1; len <= n; len++){ //
            sum += doubleElements[i + len-1];
            sums.insert(sum);
        }
        
    }
    return sums.size();
}