#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    vector<int> vec;
    int res = 0, k = 0;
    int n; cin >> n;

    for(int i = 0; i<n; i++){
        cin >> k;
        vec.push_back(k);
    }
    sort(vec.begin(), vec.end(), greater<int>());

    for(int i = 0; i<n; i++){
        res += vec[i]*(i+1);
    }
    cout << res;
}