#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> v;
    int k;
    
    for(int i = 0; i < 10; i++) {
        cin >> k;
        k %= 42;
        bool flag = true;
        for(int p = 0; p < v.size(); p++){
            if(k == v[p]) flag = false;    
        }
        if(flag == true) v.push_back(k%42);
        
        }
        cout << v.size();
        return 0;
    }