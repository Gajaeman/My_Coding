#include <iostream>
using namespace std;
int tc;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cin >> tc; int k = 0;
    for (int p = 0; p < tc; p++) {
        int res = 0;
        cin >> k;
        if (k < 5) {
            cout << 0 << "\n";
        }
        else {
            for (int j = 5; j <= k; j*=5){
                res += k/j;
            }
            cout << res << "\n";
        }
    }
    return 0;
}

/*Timeout
#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
int tc;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cin >> tc; int k = 0;
    for (int p = 0; p < tc; p++) {
        int res = 0;
        cin >> k;
        if (k < 5) {
            cout << 0 << endl;
        }
        else {
            for (int j = 5; j <= k; j+5) {
                int temp = j;
                while (temp % 5 == 0 && temp > 4) {
                    res += 1;
                    temp /= 5;
                }
            }
            cout << res << endl;
        }
    }
    return 0;
}
*/