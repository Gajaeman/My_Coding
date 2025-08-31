#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int gcd(int a, int b){
    if(a==0) return b;
    return gcd(b%a,a);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n = 0, num = 0;
    int t = 0; cin >> t;
    vector<int> v;

    for(int i = 0; i < t; i++){
        cin >> n;
        v.clear();
        for(int j = 0; j < n; j++){
            cin >> num;
            v.push_back(num);
        }
        long long res = 0;
        for(int i = 0; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                res += gcd(v[i],v[j]);
            }
        }
        cout << res << '\n';
    }
    return 0;
}