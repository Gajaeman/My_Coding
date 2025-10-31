#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T; 
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        int cnt = 0;

        for (int b = 2; b < n; b++) {
            for (int a = 1; a < b; a++) {
                int ja = (a*a + b*b + m);
                int mo = a*b;           
                if (ja % mo == 0) cnt++;
            }
        }
        cout << cnt << '\n';
    }
}