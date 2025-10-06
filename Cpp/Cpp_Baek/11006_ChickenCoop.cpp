#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int t;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, m = 0;
        cin >> n >> m;
        int u = 2 * m - n;
        int t = m - u;
        cout << u <<" "<< t << endl;
    }
}