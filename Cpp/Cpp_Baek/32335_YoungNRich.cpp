#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m, lev = 0;
    string pw;
    bool ck = true;
    cin >> n >> m >> pw;

    vector<int> v(n);
    for (int i = 0; i < n; i++) v[i] = pw[i] - '0';
    
    while (lev < n && m > 0) {
        int need = (10 - v[lev]) % 10;
        if (need <= m) {
            m -= need;
            v[lev] = 0;
        }
        lev += 1;
    }
    for(int i=0; i<n; i++) if(v[i] != 0) ck = false;
    if(ck) v[n-1] = m%10;
    else v[n] += m;

    for (int i = 0; i < n; i++) cout << v[i];
    return 0;
}